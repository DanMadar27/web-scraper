import sys
sys.path.append('.') # Add root directory to Python path

import unittest
from src.tests.test_scraper import TestScraper

if __name__ == '__main__':
    # Create a test suite and add the test cases from each module
    suite = unittest.TestLoader().loadTestsFromTestCase(TestScraper)

    # Add other test cases to the suite as needed
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestModule2))

    # Run the test suite with verbosity set to 2 for detailed output
    unittest.TextTestRunner(verbosity = 2).run(suite)
