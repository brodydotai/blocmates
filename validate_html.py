
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


from html.parser import HTMLParser
import re

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.self_closing = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.stack = []
        self.errors = []
        self.lineno = 1
        
    def getpos(self):
        return self.lineno
        
    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.stack.append((tag, self.lineno))
    
    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if self.stack:
            last_tag, last_line = self.stack.pop()
            if last_tag != tag:
                self.errors.append(f"Mismatched tags: <{last_tag}> (line {last_line}) closed with </{tag}> (line {self.lineno})")
        else:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.lineno}")
    
    def check_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple line counter for error reporting
        lines = content.split('\n')
        
        # Parse HTML
        try:
            self.feed(content)
        except Exception as e:
            self.errors.append(f"Parse error: {e}")
        
        # Check for unclosed tags
        if self.stack:
            for tag, line in self.stack:
                self.errors.append(f"Unclosed tag <{tag}> at line {line}")
        
        return self.errors

validator = HTMLValidator()
errors = validator.check_file('app/blocmates-show-prep.html')

if errors:
    print("HTML Validation Errors Found:")
    for err in errors[:20]:  # Show first 20 errors
        print(f"  - {err}")
else:
    print("No HTML validation errors found!")