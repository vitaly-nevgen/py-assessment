import unittest

from tests.types import *
from tests.functions import *
from tests.classes import *
from tests.arrays import *
from tests.strings import *

try:
    from tests.develop import *
except:
    pass

unittest.main()