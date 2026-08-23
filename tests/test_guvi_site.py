import pytest
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

needs_login = pytest.mark.skipif(
    not Config.VALID_EMAIL or not Config.VALID_PASSWORD,
    reason="ashiqofficial786@gmail.com / Inara@123 in .env to run this test",
)


def test_case_01_url_is_valid(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    assert Config.BASE_URL in home.get_current_url()


def test_case_02_page_title_is_correct(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    assert home.get_title() == Config.EXPECTED_TITLE


def test_case_03_login_button_visible_and_clickable(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    assert home.is_login_button_visible()
    home.click_login()


def test_case_04_signup_button_visible_and_clickable(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    assert home.is_signup_button_visible()
    home.click_signup()


def test_case_05_signup_redirects_to_register_page(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    home.click_signup()
    assert home.wait_for_url_contains("register")
    assert RegisterPage(page).is_loaded()

@needs_login
def test_case_06_login_with_valid_credentials(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    home.click_login()
    login = LoginPage(page)
    login.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
    assert home.is_logged_in()

def test_case_07_login_with_invalid_credentials(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    home.click_login()
    login = LoginPage(page)
    login.login(Config.INVALID_EMAIL, Config.INVALID_PASSWORD)
    login.get_error_message()



def test_case_08_menu_items_are_displayed(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    visible = home.are_menu_items_visible()
    assert all(visible.values()), visible


def test_case_09_dobby_assistant_present(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    assert home.is_dobby_assistant_present()


@needs_login
def test_case_10_logout_functionality(page):
    home = HomePage(page)
    home.load(Config.BASE_URL)
    home.click_login()
    LoginPage(page).login(
        Config.VALID_EMAIL,
        Config.VALID_PASSWORD
    )
    home.click_logout()
    assert not home.is_logged_in()