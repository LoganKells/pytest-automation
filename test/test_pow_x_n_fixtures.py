import pytest
import selenium
from selenium import webdriver
from time import sleep
import math
import os
import sys
from pathlib import Path
project_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str(project_root))
from src.pow_x_n import power


# We can use fixtures to load the Selenium WebDriver with dependency injection.
# https://www.selenium.dev/documentation/webdriver/
@pytest.fixture(scope="class")
def init_chrome_webdriver(request):
    driver = selenium.webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver")
    request.cls.driver = driver
    yield  # return a generator
    driver.close()


# We can use fixtures to set up the inputs with dependency injection.
# https://docs.pytest.org/en/6.2.x/fixture.html
@pytest.fixture(scope="module")
def resource_setup():
    test_cases = ((x, n, math.pow(x, n)) for x in range(10) for n in range(12))  # Generator
    return test_cases


# Run all tests in terminal:
#   pytest --capture=no --verbose --html=pytest_selenium_test_pow_x_n_fixtures.html test_pow_x_n_fixtures.py
@pytest.mark.usefixtures("init_chrome_webdriver")
class TestPower:
    def test_power_fixture(self, resource_setup):
        for x, n, expected in resource_setup:
            assert power(x, n) == expected
        print(self.driver.title)
        # sleep(3)


if __name__ == "__main__":
    pytest.main(["py.test.exe --capture=no --verbose --html=pytest_selenium_test_pow_x_n_fixtures.html test_pow_x_n_fixtures.py"])