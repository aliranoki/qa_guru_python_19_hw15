"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from pages.login_page import LoginPage


def test_github_desktop(desktop_screen):
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_desktop()


def test_github_mobile(mobile_screen):
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_mobile()