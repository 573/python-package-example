import unittest
import python_package_example

class BaseTest(unittest.TestCase):
    def test_range(self):
        p = python_package_example.base_run()
        assert type(p) is list
        assert len(p) >= 0 and len(p) <= 3

def test_suite():
    return unittest.makeSuite(BaseTest)
