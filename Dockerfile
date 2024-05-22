FROM python:3.12.3-alpine3.19

# update apk repo
RUN echo "https://dl-cdn.alpinelinux.org/alpine/latest-stable/main" >> /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories

# install packages (chromium, chromedriver, tzdata, jdk, curl, tar, allure)
RUN apk update && \
    apk add --no-cache chromium chromium-chromedriver tzdata openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

WORKDIR /usr/workspace
COPY requirements.txt .
RUN pip install -r requirements.txt