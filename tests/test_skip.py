"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from pages.login_page import LoginPage


def test_github_desktop(setup_browser):
    if setup_browser == "mobile":
        pytest.skip()
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_desktop()


def test_github_mobile(setup_browser):
    if setup_browser == "desktop":
        pytest.skip()
    login_page = LoginPage()
    login_page.open()
    login_page.should_signup_button_on_mobile()