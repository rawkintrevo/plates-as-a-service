# Dockerfile for example whisk docker action
FROM openwhisk/dockerskeleton
 
ENV FLASK_PROXY_PORT 8080

### Add source file(s)
ADD openalpr-wrapper.py /action/openalpr-wrapper.py
ADD exec.sh /action/exec
RUN chmod +x /action/exec

RUN apk add --no-cache --virtual .build-deps \
        bzip2-dev \
        gcc \
        libc-dev \
#	### Compile source file(s)
# && cd /action; gcc -o exec example.c \
# && apk del .build-deps

RUN  # Enable testing repo
        echo "http://nl.alpinelinux.org/alpine/edge/testing" >>/etc/apk/repositories \
        # Install needed libs
     && apk --no-cache add \
        libexecinfo libcurl leptonica log4cplus opencv tesseract-ocr \
        libcanberra-gtk3 ttf-freefont \
        # Install build dependencies
     && apk --no-cache add --virtual .build-deps \
        ca-certificates wget \
        git gcc g++ cmake make curl-dev leptonica-dev log4cplus-dev opencv-dev tesseract-ocr-dev libexecinfo-dev \
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

CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]
