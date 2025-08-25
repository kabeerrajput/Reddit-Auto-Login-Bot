# Selenium Reddit Auto Login Bot
This project is a Python-based bot that uses the Selenium library to automate the login process on Reddit. It is structured into two main classes: SeleniumUtils and RedditBot.

## Prerequisites
Before running the bot, you need to have the following installed:
- Python 3.x
- Selenium library: You can install it using pip:
  * pip install selenium

A web driver: This bot uses chromedriver. Make sure you have the correct version of chromedriver that matches your Google Chrome browser version. You can download it from the official ChromeDriver website.

## Project Structure
- main.py: The entry point of the application. It initializes and runs the RedditBot.

- Reddit_Bot.py: Contains the RedditBot class, which handles the specific automation tasks for Reddit, such as logging in.

- Selenium_Utils.py: A utility class, SeleniumUtils, with a collection of reusable methods for common Selenium actions like navigating to a URL, waiting for elements, clicking, and filling out forms.

## Getting Started
### 1. Clone the repository:
* git clone https://github.com/your-repo/selenium-reddit-bot.git
cd selenium-reddit-bot

### 2. Configure your Reddit credentials:
Open Reddit_Bot.py and enter your Reddit username and password in the __username and __password variables.
* class RedditBot:<br>
    __username = "YOUR_REDDIT_USERNAME"<br>
    __password = "YOUR_REDDIT_PASSWORD"<br>

### 3. Run the bot:
Execute the main.py file from your terminal:
* python main.py

The bot will open a new Chrome browser window, navigate to Reddit, and attempt to log in using the credentials you provided.


## Core Components
Selenium_Utils.py
This file defines the SeleniumUtils class, which provides a set of helper functions for interacting with web elements.

- go_to_url(url): Navigates the browser to the specified URL.

- wait_for_element_presence(xpath): Waits until an element is present on the page.

- click_element(xpath): Clicks on an element.

- fill_keys_value(xpath, keys_value): Fills a text input field with the given value.

- get_element(xpath): Finds and returns a single web element.

## Reddit_Bot.py
This file contains the main logic for the Reddit automation.

- __init__(): Initializes the SeleniumUtils object and starts the automation process by calling execute_process().

- login(): A method that navigates to the Reddit login page, waits for the login form elements, and fills in the username and password fields. It then attempts to click the login button to complete the process. The code also includes commented-out alternative methods for handling different element types, such as Shadow DOM elements.

This simple script is the entry point for the bot. It creates an instance of the RedditBot class, which in turn runs the entire automation sequence.





