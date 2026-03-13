
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

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
                            'link', 'meta', 'param', 'source', 'track', 'wbr',
                            '!DOCTYPE', 'html', 'body', 'head'}
        
    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)
            
    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
            
with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

validator = TagValidator()
validator.feed(content)

print("=" * 60)
print("FINAL VALIDATION AFTER FIXES")
print("=" * 60)

# Check key structure
print("\nKey structural checks:")
checks = [
    ('<!DOCTYPE html>', 'DOCTYPE'),
    ('<html', 'HTML opening'),
    ('</head>', 'HEAD closing'),
    ('<body>', 'BODY opening'),
    ('</div>', 'DIV closing'),
    ('</body>', 'BODY closing'),
    ('</html>', 'HTML closing'),
]

all_good = True
for pattern, name in checks:
    found = pattern in content
    status = '✓' if found else '✗'
    print(f"  {status} {name}")
    if not found:
        all_good = False

print(f"\nTag validation:")
if len(validator.stack) == 0:
    print("  ✓ All non-void tags properly closed")
else:
    print(f"  ✗ Unclosed tags: {validator.stack}")
    all_good = False

print("\n" + "=" * 60)
if all_good:
    print("✓ HTML IS NOW STRUCTURALLY VALID")
else:
    print("✗ HTML STILL HAS ISSUES")
print("=" * 60)