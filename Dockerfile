FROM python

# install packages (chromium, tzdata, openjdk, curl, tar)
RUN apt-get update && \
    apt-get install -y chromium tzdata openjdk-17-jre curl tar && \
    curl -o allure-2.29.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.29.0/allure-commandline-2.29.0.tgz && \
    tar -zxvf allure-2.29.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure && \
    rm allure-2.29.0.tgz

WORKDIR /test_project

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# CMD pytest -sv --alluredir=allure-results