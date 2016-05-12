import unittest
from timingdecorator.timeit import timeit
import time

class TestTimeit(unittest.TestCase):
    def setUp(self):
        pass


    @timeit
    def test_timeit(self):
        time.sleep(2)