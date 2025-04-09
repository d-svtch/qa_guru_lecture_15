"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, by


@pytest.fixture(params=[(1920, 1080), (414, 489)])
def browser_preps(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize("browser_preps", [(1920, 1080)], indirect=True)
def test_github_desktop(browser_preps):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("browser_preps", [(414, 489)], indirect=True)
def test_github_mobile(browser_preps):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
