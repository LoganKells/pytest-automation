# pytest-automation
This project uses PyTest and Selenium to achieve test automation with a web service HTML report.

!["Example Selenium Report"](https://sn3301files.storage.live.com/y4mU__vM76eqa2_FfE6r09FujWagj1uWddruivwyM7suLKRZRC1b7mY0vB0Dhi-tvX_b7oavSkQgBDP1VwK2xzMqhJRtXhpo2Jdj4f2eROe6EIXHxzS0Kg-7Z79lqsZEwE2K3_HhAzGgKJAMLp4dtTXhgLWzRKjN8nxO4EQB3AkRqesVsnf5FYBmjIDRXyP7teo?width=1024&height=529&cropmode=none)

## Installation

<ol>
<li>Clone the repo.</li>
<li>Install dependencies indicated in requirements.txt.</li>
<li>In addition, download the Chromium drivers from here and add the driver path to your PATH.
https://chromedriver.chromium.org/downloads</li>
</ol>

## Run the test automation report
The test automation can be initiated with test_pow_x_n_fixtures.py in command line with these arguments. 
If we run this command line process on an interval, then we have a report that is updated each run.


    pytest --capture=no --verbose --html=pytest_selenium_test_pow_x_n_fixtures.html test_pow_x_n_fixtures.py

Files needed:

<ul>
<li>Report: pytest_selenium_test_pow_x_n_fixtures.html</li>
<li>Python file: ./test/test_pow_x_n_fixtures.py</li>
</ul>


