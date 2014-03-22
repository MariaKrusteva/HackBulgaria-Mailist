import unittest
from mailList import MailList
from mailListManager import MailListManager


class TestFunctionality(unittest.TestCase):

    def test_create(self):
        list = MailListManager()
        list.create("listec")
        self.assertEqual(True, isinstance(MailList, list.maillists[0][1]))


if __name__ == "__main__":
    unittest.main()
