from playwright.sync_api import TimeoutError as PWTimeout
from config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(Config.TIMEOUT)

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        try:
            self.page.locator(locator).first.click()
        except PWTimeout:
            logger.error("Click failed: %s", locator)
            raise

    def type_text(self, locator, text):
        try:
            self.page.locator(locator).first.fill(text)
        except Exception:
            logger.error("Type failed: %s", locator)
            raise

    def is_visible(self, locator):
        try:
            self.page.locator(locator).first.wait_for(state="visible")
            return True
        except PWTimeout:
            return False

    def get_text(self, locator):
        try:
            return self.page.locator(locator).first.inner_text().strip()
        except Exception:
            return ""

    def get_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url

    def wait_for_url_contains(self, fragment):
        import re

        try:
            self.page.wait_for_url(
                re.compile(fragment),
                timeout=Config.TIMEOUT
            )
            return True
        except PWTimeout:
            return False