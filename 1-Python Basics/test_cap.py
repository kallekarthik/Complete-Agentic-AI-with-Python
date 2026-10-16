import cap
import unittest

class Testcap(unittest.TestCase):

    def test_oneword(self):
        text = 'python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiwords(self):
        text='faith can move mountains'
        result=cap.cap_text(text)
        self.assertEqual(result,'Faith Can Move Mountains')

if __name__=='__main__':
    unittest.main()


