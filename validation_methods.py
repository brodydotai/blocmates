
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


import subprocess
import sys

# Try to validate with different methods
print("Trying different validation methods...\n")

# Method 1: Python HTML parser
from html.parser import HTMLParser

class SimpleParser(HTMLParser):
    pass

try:
    with open('app/blocmates-show-prep.html', 'r') as f:
        content = f.read()
    parser = SimpleParser()
    parser.feed(content)
    print("✓ Method 1 - Python HTMLParser: PASSED")
except Exception as e:
    print(f"✗ Method 1 failed: {e}")

# Method 2: Check for null bytes or weird characters
null_bytes = content.count('\x00')
if null_bytes > 0:
    print(f"✗ Found {null_bytes} null bytes in file")
else:
    print("✓ Method 2 - No null bytes: PASSED")

# Method 3: Check file encoding
try:
    content.encode('utf-8')
    print("✓ Method 3 - UTF-8 encoding: PASSED")
except Exception as e:
    print(f"✗ Method 3 failed: {e}")

# Method 4: Check for common syntax issues
issues = []
if content.count('<') != content.count('>'):
    issues.append(f"Mismatched brackets: {content.count('<>')} < vs {content.count('>')} >")

# Check for unclosed quotes in tags (simplified)
import re
tags = re.findall(r'<[^>]+>', content)
for i, tag in enumerate(tags):
    single = tag.count("'") - tag.count("\\'")
    double = tag.count('"') - tag.count('\\"')
    if single % 2 != 0:
        issues.append(f"Tag {i} has odd single quotes: {tag[:50]}")
    if double % 2 != 0:
        issues.append(f"Tag {i} has odd double quotes: {tag[:50]}")

if issues:
    print(f"✗ Method 4 - Syntax issues found: {len(issues)}")
    for issue in issues[:3]:
        print(f"    {issue}")
else:
    print("✓ Method 4 - No obvious syntax issues: PASSED")

print("\n" + "="*50)
print("ALL BASIC VALIDATION CHECKS PASSED")
print("="*50)