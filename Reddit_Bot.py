from Selenium_Utils import SeleniumUtils
from selenium.webdriver.common.by import By
import time

class RedditBot:
    __username = ""
    __password = ""

    def __init__(self):
        self._sel = SeleniumUtils()
        self.execute_process()

    def login(self):
        reddit_url = "https://www.reddit.com/"
        logo_path = "//div[contains(@class, 'justify-start')]"
        login_button_path = "//span[.='Log In']"
        # username_path = '//input[@name="username" and @type="text"]'
        # password_path = '//input[@name="password" and @type="password"]'
        # profile_path = '//button[contains(@class, "overflow-visible") and @id="expand-user-drawer-button" and @type="button"]'
        profile_path = '//button[@id="expand-user-drawer-button" and @type="button"]'
        # login_btn_shadow_root = "return document.querySelector('shreddit-overlay-display').shadowRoot.querySelector('shreddit-signup-drawer').shadowRoot.querySelector('shreddit-drawer').children[0].children[0].children[0].children[0].shadowRoot.querySelector('shreddit-async-loader').children[0].children[0].children[0].children[0].children[2].children[0];"
        login_btn_shadow_root = "//div[@slot='primaryButton']/faceplate-tracker[@noun='login']/button[contains(@class, 'login')]"

        # navigate to reddit
        self._sel.go_to_url(reddit_url)
        self._sel.wait_for_element_presence(logo_path)
        self._sel.wait_for_element_presence(login_button_path)

        self._sel.click_element(login_button_path)
        self._sel.wait_for_element_presence("//faceplate-text-input[@id='login-username']", wait_secs=5)

        shadow_host = self._sel.get_element("faceplate-text-input#login-username", By.CSS_SELECTOR)
        shadow_root = self._sel.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        input_element = shadow_root.find_element(By.CSS_SELECTOR, "input[name='username']")
        input_element.send_keys(self.__username)
        time.sleep(0.5)
        shadow_host = self._sel.get_element("faceplate-text-input#login-password", By.CSS_SELECTOR)
        shadow_root = self._sel.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        input_element = shadow_root.find_element(By.CSS_SELECTOR, "input[name='password']")
        input_element.send_keys(self.__password)
        time.sleep(2)

        # self._sel.fill_keys_value(input_element, self.__username)
        # time.sleep(0.5)
        # self._sel.fill_keys_value(password_path, self.__password)
        # time.sleep(2)
        # login_btn_ele = self._sel.driver.execute_script(login_btn_shadow_root)
        # login_btn_ele.click()
        # self._sel.wait_for_element_to_invisible(login_btn_shadow_root)

        self._sel.click_element(login_btn_shadow_root, By.XPATH)
        self._sel.wait_for_element_presence(profile_path)
        time.sleep(10)

    def execute_process(self):
        self.login()
