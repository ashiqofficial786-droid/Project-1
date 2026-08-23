from pages.base_page import BasePage


class HomePage(BasePage):
    LOGIN_BUTTON = "text=/login/i"
    SIGNUP_BUTTON = "text=/sign.?up/i"
    NAV_COURSES = "text=/courses/i"
    NAV_LIVE_CLASSES = "text=/live classes/i"
    NAV_PRACTICE = "text=/practice/i"
    DOBBY_ASSISTANT = "#zsiq_float, #zs_fl_chat, [aria-label='Chat Widget']"
    PROFILE_AVATAR = "img[alt='Profile' i]"
    ACCOUNT_DROPDOWN = "#account-boxheader"

    def load(self, url):
        self.open(url)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def is_login_button_visible(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def is_signup_button_visible(self):
        return self.is_visible(self.SIGNUP_BUTTON)

    def are_menu_items_visible(self):
        visible = {
            "courses": self.is_visible(self.NAV_COURSES),
            "live_classes": self.is_visible(self.NAV_LIVE_CLASSES),
            "practice": self.is_visible(self.NAV_PRACTICE)
        }

        return visible

    def is_dobby_assistant_present(self):
        return self.is_visible(self.DOBBY_ASSISTANT)

    def is_logged_in(self):
        return self.is_visible(self.PROFILE_AVATAR)

    def click_logout(self):
        self.page.wait_for_selector(self.PROFILE_AVATAR, state="visible", timeout=15000)
        self.click(self.PROFILE_AVATAR)
        self.page.wait_for_selector(self.ACCOUNT_DROPDOWN, state="visible", timeout=10000)
        self.page.locator(self.ACCOUNT_DROPDOWN).get_by_text("Sign Out").click()
        self.page.wait_for_selector(
            self.LOGIN_BUTTON,
            state="visible",
            timeout=10000
        )