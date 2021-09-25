import unittest
from hello import hello_name


class TestHello(unittest.TestCase):
    def test_hello_name(self):
        self.assertEqual(hello_name('Max'), 'Hello Max')


# if __name__ == '__main__':
#     unittest.main()
