FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN apt-get install -y nano mc curl htop wget --fix-missing
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update && apt-get install -y python3.6 python3.6-dev python3.6-venv
RUN apt-get install -y libcurl4-openssl-dev libssl-dev gcc clang build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev libgeos-dev  pkg-config libfreetype6-dev \
    libsm6 libxext6 libxrender-dev
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3
RUN mkdir app
WORKDIR /app
RUN wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/supervised_models/lid.176.bin
COPY requirements.txt requirements.txt
RUN python3.6 -m pip install cython && python3.6 -m pip install --upgrade cython
RUN python3.6 -m pip install -r requirements.txt
COPY src src
COPY server.py server.py
CMD python3.6 -u server.py

HEALTHCHECK --interval=3s --timeout=5s \
  CMD curl -f http://localhost:9779/langindentification/healthcheck || exit 1