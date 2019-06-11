from . import FrogJump
import unittest

class FrogJumpTest(unittest.TestCase):

    def setUp(self):
        self.frog = FrogJump.FrogJump()

    def test_cry(self):
        self.assertEqual(self.frog.cry(), '개굴')

    def test_jump_negative(self):
        self.assertRaises(Exception, self.frog.jump(10, 85, -30))

    def test_jump(self):
        self.assertEqual(3, self.frog.jump(10, 85, 30))

if __name__ == '__main__':
    unittest.main()