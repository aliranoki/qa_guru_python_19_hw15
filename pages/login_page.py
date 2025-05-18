from selene import browser, be, have


class LoginPage:

    def open(self):
        browser.open('https://github.com/')

    def should_signup_button_on_desktop(self):
        browser.element('//a[contains(text(), "Sign up")]').should(be.visible).click()


    def should_signup_button_on_mobile(self):
        browser.element('[class="Button-content"]').click()
        browser.element('//a[contains(text(), "Sign up")]').should(be.visible).click()
