FROM ubuntu:16.04
RUN apt update \
        && apt install -y python3-pip python3-dev vim \
        && pip3 install tensorflow \
        && pip3 install tensorflow-gpu \
        && ln -s /usr/bin/python3 /usr/bin/python \
        && ln -s /usr/bin/pip3 /usr/bin/pip

# Ó³Éä¶Ë¿Ú
EXPOSE 8888
