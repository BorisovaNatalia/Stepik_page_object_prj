from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_HEADER = (By.CSS_SELECTOR, ".product_main>h1")
    ALERT_SUCCESS_MESSAGES = (By.CSS_SELECTOR,".alert-success > .alertinner  > strong")
    ALERT_INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info > .alertinner  > p > strong")
    PRICE_LABLE = (By.CSS_SELECTOR, ".product_main>.price_color")