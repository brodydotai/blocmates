
import sys, pytest, collections, collections.abc, urllib3.exceptions, _pytest.pytester, numpy;
collections.Mapping = collections.abc.Mapping;
collections.MutableMapping = collections.abc.MutableMapping;
collections.MutableSet = collections.abc.MutableSet;
collections.Sequence = collections.abc.Sequence;
collections.Callable = collections.abc.Callable;
collections.Iterable = collections.abc.Iterable;
collections.Iterator = collections.abc.Iterator;
urllib3.exceptions.SNIMissingWarning = urllib3.exceptions.DependencyWarning;
pytest.RemovedInPytest4Warning = DeprecationWarning;
_pytest.pytester.Testdir = _pytest.pytester.Pytester;
numpy.PINF = numpy.inf;
numpy.unicode_ = numpy.str_;
numpy.bytes_ = numpy.bytes_;
numpy.float_ = numpy.float64;
numpy.string_ = numpy.bytes_;
numpy.NaN = numpy.nan;


import re

with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

print("Checking for HTML syntax issues...\n")

issues = []

# Check for unclosed quotes in attributes
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    # Count quotes outside of tags (simplified check)
    in_tag = False
    quote_char = None
    for j, char in enumerate(line):
        if char == '<' and not in_tag:
            in_tag = True
        elif char == '>' and in_tag:
            in_tag = False
            quote_char = None
        elif in_tag and char in '\'"':
            if quote_char is None:
                quote_char = char
            elif quote_char == char:
                quote_char = None
    
    if quote_char is not None:
        issues.append(f"Line {i}: Potential unclosed quote in tag")

# Check for unescaped < or > in content
for i, line in enumerate(lines, 1):
    # Look for lone < or > that might be issues
    if re.search(r'(?<!<[^>]*)<(?![^>]*>)', line) and '<!--' not in line:
        if not re.match(r'^\s*<', line):  # Not starting with tag
            pass  # Could be false positive

# Check for malformed entities
entities = re.findall(r'&[^;\s<>&]{0,10};', content)
invalid_entities = [e for e in entities if not re.match(r'&(?:#[0-9]+|#x[0-9a-fA-F]+|[a-zA-Z][a-zA-Z0-9]*);', e)]
if invalid_entities:
    issues.append(f"Potential invalid entities: {invalid_entities[:5]}")

# Check DOCTYPE
doctype_pattern = r'<!DOCTYPE\s+html\s*>'
if not re.search(doctype_pattern, content, re.IGNORECASE):
    issues.append("DOCTYPE may be malformed")

# Check for duplicate attributes
dup_attr_pattern = r'<\w+\s+[^>]*?(\w+)=[^>]*?\1='
matches = re.findall(dup_attr_pattern, content)
if matches:
    issues.append(f"Duplicate attributes found: {matches[:3]}")

if issues:
    print("Issues found:")
    for issue in issues[:10]:
        print(f"  - {issue}")
else:
    print("No obvious HTML syntax issues found")