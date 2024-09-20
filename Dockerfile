    # syntax=docker/dockerfile:1

    # Define image variants and versions
    ARG IMAGE_VARIANT=slim-buster
    ARG OPENJDK_VERSION=11
    ARG PYTHON_VERSION=3.10

    # Base image for Python
    FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3

    # Base image for OpenJDK
    FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

    # Install utilities and dependencies
    RUN apt-get update -y && apt-get install -y \
        dnsutils \
        curl \
        telnet \
        vim \
        git

    # Create a new user
    RUN useradd -ms /bin/bash newuser
    USER root

    # Set working directory
    WORKDIR /app

    # Copy Python from previous stage
    COPY --from=py3 / /

    # Correct ARG for PySpark
    ARG PYSPARK_VERSION=3.2.1
    RUN pip install --no-cache-dir pyspark==${PYSPARK_VERSION}

    # Copy and install Python requirements
    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt


