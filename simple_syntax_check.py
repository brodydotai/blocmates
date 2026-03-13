
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

# Check DOCTYPE
doctype_pattern = r'<!DOCTYPE\s+html\s*>'
if not re.search(doctype_pattern, content, re.IGNORECASE):
    issues.append("DOCTYPE may be malformed")
else:
    print("✓ DOCTYPE is valid")

# Check for duplicate attributes
dup_attr_pattern = r'<\w+\s+[^>]*?(\w+)=[^>]*?\1='
matches = re.findall(dup_attr_pattern, content)
if matches:
    issues.append(f"Duplicate attributes found: {matches[:3]}")
else:
    print("✓ No duplicate attributes found")

# Check for unclosed tags (basic)
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    # Simple check for odd number of quotes in a tag
    if '<' in line and '>' in line:
        tag_content = re.findall(r'<([^>]+)>', line)
        for tag in tag_content:
            single_quotes = tag.count("'")
            double_quotes = tag.count('"')
            if single_quotes % 2 != 0:
                issues.append(f"Line {i}: Odd number of single quotes in tag: <{tag[:30]}...>")
            if double_quotes % 2 != 0:
                issues.append(f"Line {i}: Odd number of double quotes in tag: <{tag[:30]}...>")

# Check for common malformed patterns
if '< <' in content:
    issues.append("Double opening bracket found")
if '> >' in content:
    issues.append("Double closing bracket found")
if '</ </' in content:
    issues.append("Double closing tag start found")

if issues:
    print("\nIssues found:")
    for issue in issues[:10]:
        print(f"  - {issue}")
else:
    print("\n✓ No obvious HTML syntax issues found")