#Basic Test Case
# Write a unittest class TestMath with one test method that checks if 2 + 3 equals 5. Setup and Teardown
#Create a test class that uses setUp() to initialize a list [1, 2, 3] and tearDown() to print
#"Test completed".
#Verify that the list length is 3 inside your test method.Multiple Assertions
#Write a test class TestStringMethods with methods to test:
#"hello".upper() equals "HELLO"
#"hello".isupper() returns False
#Exception Testing
#Use assertRaises to verify that dividing by zero (10 / 0) raises a ZeroDivisionError.
#Test Suite Execution
#Create two test classes (TestAdd and TestSubtract) and combine them into a single test
#suite using unittest.TestSuite.
#Run the suite using unittest.TextTestRunner().




import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)


class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_length(self):
        self.assertEqual(len(self.data), 3)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())


class TestException(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)



if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestSuite()

    # Add test classes
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    # Run tests
    runner = unittest.TextTestRunner()
    runner.run(suite)