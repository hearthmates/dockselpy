FROM ubuntu:latest

# install system dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libu2f-udev \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libvulkan1 \
    curl unzip wget \
    xvfb libgbm1

# install firefox

RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    apt-get purge firefox && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP

# install google-chrome
RUN CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP

# install python dependencies
RUN pip3 install selenium
RUN pip3 install pyvirtualdisplay
RUN pip3 install webdriver-manager

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/

COPY example.py example.py
COPY install_webdrivers.py install_webdrivers.py

RUN python3 install_webdrivers.py

EXPOSE 4444

CMD ./example.py
