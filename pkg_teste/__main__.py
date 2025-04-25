""" main entry point """
import sys

if sys.argv[0].endswith("__main__.py"):
 sys.argv[0] = "py -m pkg_teste"

#print(*sys.argv, sep="| ")
from . import _test as main
main()
