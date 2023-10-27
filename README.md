# Web Scraper
Telegram bot that extracts data about video games.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
Before you begin, ensure you have the following installed:

- Python runtime environment
- pip - Python installer for Python
- Telegram Bot Token - Obtain from [BotFather](https://core.telegram.org/bots#botfather)

### Installing
Follow these steps to set up the development environment:

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Make sure you have [wkhtmltopdf](https://wkhtmltopdf.org/) installed and configured in your computer's [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) environment variable.
4. Copy `.env.example` to `.env` and configure your environment variables
5. Run the bot using `python main.py`

### VS Code

If you like to run the program using VS Code, you can create `launch.json` file in `.vscode` folder:

```json
{
  "version": "0.2.0",
  "configurations": [

    {
      "name": "Launch",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/main.py",
      "console": "integratedTerminal"
    },
    {
      "name": "Test",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/tests/run_tests.py",
      "console": "integratedTerminal"
    }
  ]
}
```

## Tests
To execute the tests, run `python src/tests/run_tests.py` or `python src/tests/test_module.py`.

## Commands

The Telegram bot is interacted by the following commands:

1. **/start**: Show a welcome message
2. **/help**: Show possible commands
3. **/updates**: Get the latest patch notes of Call of Duty