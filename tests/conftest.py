import pytest
from playwright.sync_api import sync_playwright
from config import Config


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser_type = getattr(p, Config.BROWSER)
        browser = browser_type.launch(headless=Config.HEADLESS)
        try:
            pg = browser.new_context().new_page()
            yield pg
        finally:
            browser.close()
