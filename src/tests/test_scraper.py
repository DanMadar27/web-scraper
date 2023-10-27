import sys
sys.path.append('.') # Add root directory to Python path

import os
import unittest
from unittest.mock import patch

from src.services.scraper import export_updates
from src.config.files import OUTPUT_PATH, WEAPONS_PATH

class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up resources for all tests')
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

    @classmethod
    def tearDownClass(cls):
        print('Tearing down resources after all tests')

        if os.path.exists(OUTPUT_PATH):
            for filename in os.listdir(OUTPUT_PATH):
                file_path = os.path.join(OUTPUT_PATH, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f'Error deleting {file_path}: {e}')
            os.rmdir(OUTPUT_PATH)

    @patch('src.services.scraper.requests.get')
    def test_export(self, mock_requests_get):
        # Mock the behavior of requests.get
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.text = '''
        <div class="card-inner">
            <h1>Mock Title</h1>
            <h2>Mock Subtitle
                <a href="mock-link">
            </h2>
            <p class="dateline"> 2020-01-01 </p>
            <h3>Weapons</h3>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        '''

        export_updates()
        self.assertTrue(os.path.exists(WEAPONS_PATH))

if __name__ == '__main__':
    unittest.main()
