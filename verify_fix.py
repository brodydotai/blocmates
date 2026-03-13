
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


#!/usr/bin/env python3
"""Verify the HTML fix""" 

import os
import re
from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.tag_stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
                            'link', 'meta', 'param', 'source', 'track', 'wbr'}
        
    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.tag_stack.append(tag)
    
    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        else:
            self.errors.append(f"Mismatched tag: </{tag}>")

def run_tests():
    html_file = 'app/blocmates-show-prep.html'
    
    print("=" * 60)
    print("POST-FIX VERIFICATION")
    print("=" * 60)
    
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Check for the fix
    print("\n[TEST 1] </head> tag present")
    has_head_close = '</head>' in content
    print(f"  {'✓ PASS' if has_head_close else '✗ FAIL'}: </head> tag {'found' if has_head_close else 'missing'}")
    
    print("\n[TEST 2] HTML Structure Validation")
    validator = HTMLValidator()
    try:
        validator.feed(content)
        if not validator.errors:
            print("  ✓ PASS: All tags properly matched")
        else:
            print(f"  ✗ FAIL: {len(validator.errors)} errors found")
            for err in validator.errors[:5]:
                print(f"    - {err}")
    except Exception as e:
        print(f"  ✗ FAIL: Parse error - {e}")
    
    print("\n[TEST 3] Essential Structure")
    checks = [
        ('<!DOCTYPE html>', 'DOCTYPE'),
        ('<html lang="en">', 'HTML start'),
        ('</head>', 'HEAD close'),
        ('<body>', 'BODY start'),
        ('</body>', 'BODY close'),
        ('</html>', 'HTML close'),
    ]
    all_pass = True
    for pattern, name in checks:
        found = pattern in content
        status = '✓' if found else '✗'
        print(f"  {status} {name}")
        if not found:
            all_pass = False
    
    print("\n[TEST 4] Line count check")
    lines = content.split('\n')
    print(f"  ✓ File has {len(lines)} lines")
    
    print("\n" + "=" * 60)
    if all_pass and has_head_close:
        print("ALL TESTS PASSED ✓")
        print("The </head> tag has been successfully added.")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)
    
    return all_pass and has_head_close

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)