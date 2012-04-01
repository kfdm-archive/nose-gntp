import unittest
from nose_gntp import NoseGrowl
from nose.plugins import PluginTester


class TestSuccess(PluginTester, unittest.TestCase):
    activate = '--with-growl'
    plugins = [NoseGrowl()]

    def test_success(self):
        assert True

    def makeSuite(self):
        class TC(unittest.TestCase):
            def runTest(self):
                assert True
        return unittest.TestSuite([TC()])


class TestFailure(PluginTester, unittest.TestCase):
    activate = '--with-growl'
    plugins = [NoseGrowl()]

    def test_failure(self):
        assert False

    def makeSuite(self):
        class TC(unittest.TestCase):
            def runTest(self):
                assert True
        return unittest.TestSuite([TC()])
