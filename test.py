import unittest
from neo import Neo


class TestSuite(unittest.TestCase):

    def test(self):
        neo = Neo()
        neo.populate()
        eden = neo.eve()
        self.failIf(not eden)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
