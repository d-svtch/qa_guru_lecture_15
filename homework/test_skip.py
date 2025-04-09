"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, by


@pytest.fixture(params=[(1920, 1080), (414, 489)])
def browser_preps(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 414 or height > 489:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()


def test_github_desktop(browser_preps):
    if browser_preps == "mobile":
        pytest.skip("Тест только для desktop")
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


def test_github_mobile(browser_preps):
    if browser_preps == "desktop":
        pytest.skip("Тест только для mobile")
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
