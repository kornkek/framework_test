from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']//button/span[2]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
