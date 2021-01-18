from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert cur_url.find("login") >= 0, "Login URL is not containts 'login' word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)

        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD_FIELD), "Field  for repeat password is not presented"
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD).send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration button is not presented"
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
