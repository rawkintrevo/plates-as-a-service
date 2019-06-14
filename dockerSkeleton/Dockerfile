# Dockerfile for example whisk docker action
FROM openwhisk/dockerskeleton
 
ENV FLASK_PROXY_PORT 8080

### Add source file(s)
ADD openalpr-wrapper.py /action/openalpr-wrapper.py
ADD exec.sh /action/exec
RUN chmod +x /action/exec

### OpenAPLR, found this here (but w openCV deps): https://github.com/wallneradam/docker-openalpr-alpine

RUN \
    # Enable testing repo
    echo "http://nl.alpinelinux.org/alpine/edge/testing" >>/etc/apk/repositories \
    && apk update && apk upgrade \
    && cat /etc/apk/repositories \
    # Install needed libs
    && apk --no-cache add \
       libexecinfo libcurl leptonica log4cplus  tesseract-ocr \
       #opencv
       libcanberra-gtk3 ttf-freefont \
    # Install build dependencies
    && apk --no-cache add --virtual .build-deps \
       ca-certificates wget \
       git gcc g++ cmake make curl-dev leptonica-dev log4cplus-dev  tesseract-ocr-dev libexecinfo-dev bzip2-dev libc-dev \
       # opencv-dev
    # Prepare build directories
    && cd /srv \
    && git clone https://github.com/openalpr/openalpr.git \
    && cd openalpr/src && mkdir build && cd build \
    # Patch to be able to compile with Musl glibc
    && sed -i.bak 's/backtrace/0;\/\//' ../daemon.cpp \
    # Build
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc .. && \
       make -j8 && \
       make install \
    # Clean not needed build directory and dependencies
    && rm -rf /srv/openalpr \
    && apk del .build-deps \
    # Create working directory
    && mkdir /openalpr


