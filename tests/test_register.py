from __future__ import print_function, unicode_literals
from contextlib import closing
from unittest import TestCase
from register import register


class TestRegister(TestCase):

    def setUp(self):
        """
        Runs before each test
        """
        pass

    def tearDown(self):
        """
        Runs after each test
        """
        pass

    @classmethod
    def setUpClass(cls):
        """
        Called before tests in this class are run
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        Called after tests in this class are run
        """
        pass

    def test_register(self):

        register()
