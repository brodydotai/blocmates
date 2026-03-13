
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

# Read the HTML file
with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

# Extract JavaScript between <script> tags
script_pattern = re.compile(r'<script>(.*?)</script>', re.DOTALL)
scripts = script_pattern.findall(content)

# Combine all JavaScript
js_code = '\n'.join(scripts)

# Check for common issues
issues = []

# Check for undefined variables (basic check)
# Look for function calls that might not exist
calls = re.findall(r'(\w+)\s*\(', js_code)
calls = list(set(calls))

# Known global functions and methods
known_funcs = {'console', 'document', 'window', 'alert', 'confirm', 'prompt', 'parseInt', 'parseFloat', 
               'setTimeout', 'setInterval', 'clearTimeout', 'clearInterval', 'JSON', 'Math', 
               'Date', 'String', 'Number', 'Array', 'Object', 'Boolean', 'RegExp', 'Error',
               'twttr', 'Boolean', 'String', 'Number'}

# Functions defined in the code
defined_funcs = set(re.findall(r'function\s+(\w+)', js_code))
defined_funcs.update(re.findall(r'(?:let|const|var)\s+(\w+)\s*=\s*function', js_code))
defined_funcs.update(re.findall(r'(?:let|const|var)\s+(\w+)\s*=\s*\([^)]*\)\s*=>', js_code))

print("Functions defined:", sorted(defined_funcs))
print("\nChecking for potential issues...")

# Check for common bugs
if 'twttr.widgets.load' in js_code:
    if 'twttr' not in defined_funcs:
        print("  - Uses twttr.widgets.load but twttr is not defined (external library from twitter.com/widgets.js)")

# Check for event listeners on potentially null elements
if 'addEventListener' in js_code:
    print("  - Uses addEventListener - OK")

# Check for querySelector calls without null checks
qs_calls = re.findall(r'document\.querySelector[^;]+;', js_code)
print(f"  - Found {len(qs_calls)} querySelector calls")

# Basic syntax check - look for unmatched braces
open_braces = js_code.count('{')
close_braces = js_code.count('}')
if open_braces != close_braces:
    issues.append(f"Unmatched braces: {open_braces} open, {close_braces} close")

open_parens = js_code.count('(')
close_parens = js_code.count(')')
if open_parens != close_parens:
    issues.append(f"Unmatched parentheses: {open_parens} open, {close_parens} close")

if issues:
    print("\nIssues found:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\nNo obvious syntax issues found in JavaScript")