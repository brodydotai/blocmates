
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
import subprocess

# Read the HTML file
with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

# Extract JavaScript
script_pattern = re.compile(r'<script>(.*?)</script>', re.DOTALL)
scripts = script_pattern.findall(content)

# Combine all JavaScript
js_code = '\n'.join(scripts)

# Write to temp file and check with node
with open('/tmp/temp_check.js', 'w') as f:
    f.write(js_code)

# Try to parse with Python first (basic check)
try:
    # Check for basic syntax issues
    open_parens = js_code.count('(')
    close_parens = js_code.count(')')
    open_braces = js_code.count('{')
    close_braces = js_code.count('}')
    open_brackets = js_code.count('[')
    close_brackets = js_code.count(']')
    
    print("Bracket balance check:")
    print(f"  Parentheses: {open_parens} open, {close_parens} close - {'OK' if open_parens == close_parens else 'MISMATCH'}")
    print(f"  Braces: {open_braces} open, {close_braces} close - {'OK' if open_braces == close_braces else 'MISMATCH'}")
    print(f"  Brackets: {open_brackets} open, {close_brackets} close - {'OK' if open_brackets == close_brackets else 'MISMATCH'}")
    
    # Check for common issues
    issues = []
    
    # Check for unclosed strings (basic)
    single_quotes = js_code.count("'") - js_code.count("\\'")
    double_quotes = js_code.count('"') - js_code.count('\\"')
    
    # Look for potential issues
    if 'function function' in js_code:
        issues.append("Duplicate 'function' keyword found")
    if 'var var ' in js_code:
        issues.append("Duplicate 'var' keyword found")
    if 'let let ' in js_code:
        issues.append("Duplicate 'let' keyword found")
    if 'const const ' in js_code:
        issues.append("Duplicate 'const' keyword found")
        
    if issues:
        print("\nPotential issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\nNo obvious syntax issues detected")
        
except Exception as e:
    print(f"Error during check: {e}")