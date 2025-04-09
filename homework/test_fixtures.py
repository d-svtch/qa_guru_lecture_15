"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selene import browser, by

@pytest.fixture(params =[(1280, 720)])
def desktop_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.fixture(params =[(414, 489)])
def mobile_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

def test_github_desktop(desktop_resolution):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


def test_github_mobile(mobile_resolution):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
