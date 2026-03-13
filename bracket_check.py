
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


with open('app/blocmates-show-prep.html', 'r') as f:
    content = f.read()

# Count angle brackets more carefully
lt_count = content.count('<')
gt_count = content.count('>')

print(f"Angle bracket counts:")
print(f"  < (less than): {lt_count}")
print(f"  > (greater than): {gt_count}")
print(f"  Difference: {abs(lt_count - gt_count)}")

# Find lines with mismatched brackets
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    lt = line.count('<')
    gt = line.count('>')
    if lt != gt:
        # Check if it's in a script or style block
        print(f"Line {i}: {lt} < vs {gt} > - {line[:80]}...")