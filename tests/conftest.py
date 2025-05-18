import pytest
from selene import browser

@pytest.fixture()
def desktop_screen():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture()
def mobile_screen():
    browser.config.window_width = 412
    browser.config.window_height = 915
    yield
    browser.quit()

@pytest.fixture(scope='function', params=[(1920, 1080), (1100, 700), (768, 1024), (412, 915)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1011:
        yield "desktop"
    else:
        yield "mobile"
    browser.quit()

desktop_view = pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True)
mobile_view = pytest.mark.parametrize('setup_browser', [(412, 915)], indirect=True)