"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

from conftest import desktop_view, mobile_view
from pages.login_page import LoginPage


@desktop_view
def test_github_desktop(setup_browser):
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_desktop()


@mobile_view
def test_github_mobile(setup_browser):
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_mobile()