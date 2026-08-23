from pages.base_page import BasePage


class RegisterPage(BasePage):
    PAGE_HEADING = "h2:has-text('Sign Up')"

    def is_loaded(self) -> bool:
        try:
            self.page.wait_for_selector(self.PAGE_HEADING, timeout=10000)
            return True
        except Exception:
            return False