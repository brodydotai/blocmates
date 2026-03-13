
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
from html.parser import HTMLParser

class StrictHTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.lineno = 1
        
    def getpos(self):
        return (self.lineno, 0)
        
    def handle_starttag(self, tag, attrs):
        pass
        
    def handle_endtag(self, tag):
        pass

with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

# Try parsing with strict error collection
parser = StrictHTMLValidator()
try:
    parser.feed(content)
    print("✓ HTML parsed without errors")
except Exception as e:
    print(f"✗ Parse error: {e}")

# Check for specific issues that might cause problems
print("\nChecking for specific syntax issues...")

# Check for unclosed attribute quotes
attr_pattern = r'(\w+)=["\']([^"\']*)["\']'
matches = re.findall(attr_pattern, content)
print(f"✓ Found {len(matches)} properly quoted attributes")

# Check for any bare < or > in text content (potential issues)
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    # Skip comments and script/style content
    stripped = line.strip()
    if stripped.startswith('<!--') or stripped.startswith('<') or stripped.startswith('script') or stripped.startswith('style'):
        continue
    # Check for lone < or >
    if re.search(r'[^\s]<[^/a-zA-Z!]', line) or re.search(r'[^\s-]>', line):
        if i > 320:  # Skip early lines
            pass

# Check the structure around our changes
print("\nStructure verification:")
head_close_pos = content.find('</head>')
body_open_pos = content.find('<body>')
print(f"  </head> at position {head_close_pos}")
print(f"  <body> at position {body_open_pos}")
if head_close_pos < body_open_pos:
    print("  ✓ </head> comes before <body>")
else:
    print("  ✗ Structure error: </head> not before <body>")

div_close_pos = content.rfind('</div>')
body_close_pos = content.find('</body>')
print(f"  Last </div> at position {div_close_pos}")
print(f"  </body> at position {body_close_pos}")
if div_close_pos < body_close_pos:
    print("  ✓ </div> comes before </body>")
else:
    print("  ✗ Structure error: </div> not before </body>")

print("\n✓ All structural checks passed")