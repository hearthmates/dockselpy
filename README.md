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
