# Build an image that can do training and inference in SageMaker
# This is a Python 2 image that uses the nginx, gunicorn, flask stack
# for serving inferences in a stable way.

FROM ubuntu:18.04

MAINTAINER Amazon AI <sage-learner@amazon.com>

# RUN apt-get -y update && apt-get install -y --no-install-recommends \
#          wget \
#          nginx \
#          ca-certificates \
#     && rm -rf /var/lib/apt/lists/*


# RUN apt-get update \
#   && apt-get install -y python3-pip python3-dev \
#   && cd /usr/local/bin \
#   && ln -s /usr/bin/python3 python \
#   && pip3 install --upgrade pip \ 
#   && apt-get install git-all


# RUN pip3 --no-cache-dir install numpy opencv-python setuptools==41.0.0 pyyaml==5.1 flask torch torchvision 'git+https://github.com/facebookresearch/detectron2.git' layoutparser && \
#         rm -rf /root/.cache


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3-pip \
         python3-setuptools \
         nginx \
         ca-certificates \
         python3-dev \
         build-essential \
         manpages-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y git

RUN pip3 --no-cache-dir install --upgrade pip scikit-build cmake
RUN pip3 --no-cache-dir install numpy \
torch==1.8.1+cpu torchvision==0.9.1+cpu \
torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html \
opencv-python setuptools==41.0.0 pyyaml==5.1 flask && \
        rm -rf /root/.cache

# RUN apt-get install -y --no-install-recommends python3-dev
# RUN apt-get -y install build-essential
# RUN apt-get -y install manpages-dev
#RUN apt-get -y update

RUN pip3 --no-cache-dir install 'git+https://github.com/facebookresearch/detectron2.git' layoutparser && \
        rm -rf /root/.cache
        
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip


ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"


COPY .prima_code /opt/program
WORKDIR /opt/program