import unittest
import utilsnew


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("i run only once")

    def setUp(self) -> None:
        print("i run before every test")

    def tearDown(self) -> None:
        print("i run after all")

    def test_something(self):
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(5, utilsnew.add(2, 3))

    def test_list(self):
        self.assertEqual([1, 2, 3], utilsnew.square_list(3))


if __name__ == '__main__':
    unittest.main()
