from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "#login-btn"
    ERROR_MESSAGE = ".invalid-feedback, [class*='error' i], [class*='toast' i]"

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        print("Current URL:", self.page.url)
        print("Page text:", self.page.locator("body").inner_text())
        return ""