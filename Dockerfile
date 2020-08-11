FROM ubuntu:18.04


# Installing dependencies and repositories

RUN apt-get update
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update
RUN add-apt-repository ppa:xorg-edgers/ppa
RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cmake git pkg-config ffmpeg curl gcc g++ wget unzip zlib1g-dev libwebp-dev \
                    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev \
                    libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev uuid-dev python3-pip

RUN add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libjasper1 libjasper-dev

# Copying/installing app

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y git
RUN mkdir -p /myapp
COPY . /myapp/
RUN pip3 --no-cache-dir install -r /myapp/requirements.txt


ENTRYPOINT ["python3", "/myapp/run.py"]
