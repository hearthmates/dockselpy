## dockselpy
[![Dockselpy Stability Check](https://github.com/hearthmates/dockselpy/actions/workflows/cron.yml/badge.svg)](https://github.com/hearthmates/dockselpy/actions/workflows/cron.yml)

Docker container for running Selenium tasks using Python and the latest Chrome and Firefox drivers.

### Information

Recent struggles in finding a docker image for Selenium that supports headless versions for both Firefox and Chrome, 
led to the process of building my own version.

The image is build with the following dependencies:
- latest Chrome and chromedriver
- latest Firefox and geckodriver
- Selenium
- Python 3
- Xvfb and the python wrapper - pyvirtualdisplay


### Run using Docker:

- docker
    ```
    docker build -t dockselpy .
    docker run --privileged -p 4444:4444 -d -it dockselpy
    ```

- docker-compose

    ```
    docker-compose stop && docker-compose build && docker-compose up -d
    ```


### Use as Base Image:

- docker
    ```
    FROM hearthmates/dockselpy:latest
    ```


### Example Script

A simple python script demonstrating on how to start selenium using Firefox with custom profile or Google Chrome with desired options is provided in the source.

Note that firefox binary is located at `/opt/firefox/firefox`

- To start a firefox driver in your project:
    ```python
    # for firefox
    from selenium.webdriver import firefox
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.service import Service as FirefoxService
    
    firefox_options = firefox.options.Options()
    firefox_options.binary_location = '/opt/firefox/firefox'
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    
    # for chrome
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    ```

