import unittest
import list_functionality
from subprocess import call


class testFunctionality(unittest.TestCase):

    def addTestFiles(self):
        """
        Used for creating files (called by setUp)
        """

        self.path = "test/"
    #Creating 1st test file
        self.fileName = self.path + "testFile1"
        self.filecreate = open(self.fileName, "w")
        self.filecreate.write("rado - asdf@\ndancho - dani@\nkiro - golf@\n")
        self.filecreate.close()
    #Creating 2nd test file
        self.fileName = self.path + "testFile2"
        self.filecreate = open(self.fileName, "w")
        self.filecreate.write("rado - asdf@\ndancho - dani@\nkiro - golf@\n")
        self.filecreate.close()

    def setUP(self):
        """
        Creates some test files in the given folder
        """
        self.addTestFiles()

    def testShow_lists(self):
        self.assertEqual("[1] - testFile1\n[2] - testFile2",
                         list_functionality.show_lists(self.path))

    def tearDown(self):
        call("rm", "-r", self.path)
