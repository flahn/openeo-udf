# Use the official ubuntu:14.04 image as parent image
FROM ubuntu:18.04

# system environment
ENV DEBIAN_FRONTEND noninteractive

# Set the working directory to /tmp
WORKDIR /tmp

# Workaround for resolveconf ubuntu docker issue
# https://stackoverflow.com/questions/40877643/apt-get-install-in-ubuntu-16-04-docker-image-etc-resolv-conf-device-or-reso
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

# Install the dependencies
RUN apt update && apt upgrade -y && \
    apt install software-properties-common -y && \
    apt update && apt install --no-install-recommends --no-install-suggests \
    build-essential \
    flex \
    make \
    bison \
    gcc \
    libgcc1 \
    g++ \
    python3 \
    python3-dev \
    python3-pip \
    libpython3-all-dev \
    libgsl0-dev \
    libncurses5-dev \
    zlib1g-dev \
    gettext \
    libtiff-dev \
    libpnglite-dev \
    libcairo2 \
    libcairo2-dev \
    sqlite3 \
    libpq-dev \
    proj-data \
    gdal-bin \
    libgdal-dev \
    libspatialite7 \
    moreutils \
    iotop \
    atop \
    htop \
    iperf \
    attr \
    git \
    vim \
    curl \
    wget \
    unzip \
    zip \
    nginx \
    npm \
    bzip2 -y && \
    apt-get clean && \
    apt-get autoremove

RUN echo LANG="en_US.UTF-8" > /etc/default/locale
# RUN apt-get install nodejs-legacy
RUN npm install -g spectacle-docs

WORKDIR /tmp/src
RUN ps
RUN git clone https://github.com/Open-EO/openeo-udf.git openeo_udf
WORKDIR /tmp/src/openeo_udf
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN python3 setup.py install

CMD bash /tmp/src/openeo_udf/docker/start.sh

EXPOSE 5100
EXPOSE 5200
