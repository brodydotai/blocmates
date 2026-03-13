
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

class DetailedTagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open_tags = []
        self.errors = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
                            'link', 'meta', 'param', 'source', 'track', 'wbr'}
        
    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.open_tags.append(tag)
    
    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if self.open_tags and self.open_tags[-1] == tag:
            self.open_tags.pop()
        else:
            self.errors.append(f"Unexpected </{tag}>")

with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

# Check document structure
print("Document structure check:")
print(f"  Starts with DOCTYPE: {content.startswith('<!DOCTYPE html>')}")
html_open = '<html lang="en">' in content
print(f"  Contains html lang=en: {html_open}")
print(f"  Contains head: {'<head>' in content}")
print(f"  Contains /head: {'</head>' in content}")
print(f"  Contains body: {'<body>' in content}")
print(f"  Contains /body: {'</body>' in content}")
print(f"  Contains /html: {'</html>' in content}")

# Count key tags
print(f"\nTag counts:")
print(f"  head: {content.count('<head>')} open, {content.count('</head>')} close")
print(f"  body: {content.count('<body>')} open, {content.count('</body>')} close")
print(f"  html: {content.count('<html')} open, {content.count('</html>')} close")
print(f"  div: {content.count('<div')} open, {content.count('</div>')} close")

# Parse and check
parser = DetailedTagParser()
try:
    parser.feed(content)
    if parser.errors:
        print(f"\nParser errors found: {len(parser.errors)}")
        for err in parser.errors[:5]:
            print(f"  - {err}")
    elif parser.open_tags:
        print(f"\nUnclosed tags: {parser.open_tags}")
    else:
        print(f"\nAll tags properly closed - VALID")
except Exception as e:
    print(f"\nParse exception: {e}")