
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


import os
import re

# Check project structure
print("=== Project Structure Check ===\n")

# Check if all referenced images exist
with open('app/blocmates-show-prep.html', 'r') as f:
    html_content = f.read()

# Find all image references
img_refs = re.findall(r'images/[^"\'\s]+', html_content)
img_refs = list(set(img_refs))  # Remove duplicates

print(f"Found {len(img_refs)} image references:")
missing_images = []
for img in sorted(img_refs):
    full_path = os.path.join('app', img)
    exists = os.path.exists(full_path)
    status = "✓" if exists else "✗ MISSING"
    print(f"  {status} {img}")
    if not exists:
        missing_images.append(img)

print(f"\n=== Summary ===")
if missing_images:
    print(f"Missing images: {len(missing_images)}\n")
    for img in missing_images:
        print(f"  - {img}")
else:
    print("All referenced images exist ✓")

# Check for external resources
print("\n=== External Resources ===")
if 'fonts.googleapis.com' in html_content:
    print("  ✓ Google Fonts loaded")
if 'platform.twitter.com/widgets.js' in html_content:
    print("  ✓ Twitter widgets script loaded")

# Check for broken internal links
print("\n=== Internal Links ===")
internal_links = re.findall(r'href=["\'](?!http|#|mailto)([^"\']+)"\']', html_content)
print(f"  Found {len(internal_links)} internal link references")

print("\n=== Overall Status ===")
if not missing_images:
    print("✓ Project structure appears correct")
else:
    print("✗ Some issues found")