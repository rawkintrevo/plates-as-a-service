# Dockerfile for example whisk docker action
FROM openwhisk/dockerskeleton
 
ENV FLASK_PROXY_PORT 8080

### Add source file(s)
ADD openalpr-wrapper.py /action/openalpr-wrapper.py
ADD exec.sh /action/exec
RUN chmod +x /action/exec

## Open CV build found this here: https://hub.docker.com/r/julianbei/alpine-opencv-microimage/dockerfile

RUN echo -e '@edgunity http://nl.alpinelinux.org/alpine/edge/community\n\
@edge http://nl.alpinelinux.org/alpine/edge/main\n\
@testing http://nl.alpinelinux.org/alpine/edge/testing\n\
@community http://dl-cdn.alpinelinux.org/alpine/edge/community'\
  >> /etc/apk/repositories

RUN apk add --update --no-cache \
  # --virtual .build-deps \
      build-base \
      openblas-dev \
      unzip \
      wget \
      cmake \
      #Intel® TBB, a widely used C++ template library for task parallelism'
      libtbb@testing  \
      libtbb-dev@testing   \
      # Wrapper for libjpeg-turbo
      libjpeg  \
      # accelerated baseline JPEG compression and decompression library
      libjpeg-turbo-dev \
      # Portable Network Graphics library
      libpng-dev \
      # A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard (development files)
      jasper-dev \
      # Provides support for the Tag Image File Format or TIFF (development files)
      tiff-dev \
      # Libraries for working with WebP images (development files)
      libwebp-dev \
      # A C language family front-end for LLVM (development files)
      clang-dev \
      linux-headers \
      && pip install numpy

ENV CC /usr/bin/clang
ENV CXX /usr/bin/clang++

ENV OPENCV_VERSION=3.1.0

RUN \
	#mkdir /opt && cd /opt && \
	cd opt && \
  wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
  unzip ${OPENCV_VERSION}.zip && \
  rm -rf ${OPENCV_VERSION}.zip

RUN mkdir -p /opt/opencv-${OPENCV_VERSION}/build && \
  cd /opt/opencv-${OPENCV_VERSION}/build && \
  cmake \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D WITH_FFMPEG=NO \
  -D WITH_IPP=NO \
  -D WITH_OPENEXR=NO \
  -D WITH_TBB=YES \
  -D BUILD_EXAMPLES=NO \
  -D BUILD_ANDROID_EXAMPLES=NO \
  -D INSTALL_PYTHON_EXAMPLES=NO \
  -D BUILD_DOCS=NO \
  -D BUILD_opencv_python2=NO \
  -D BUILD_opencv_python3=ON \
  -D PYTHON3_EXECUTABLE=/usr/local/bin/python \
  -D PYTHON3_INCLUDE_DIR=/usr/local/include/python3.6m/ \
  -D PYTHON3_LIBRARY=/usr/local/lib/libpython3.so \
  -D PYTHON_LIBRARY=/usr/local/lib/libpython3.so \
  -D PYTHON3_PACKAGES_PATH=/usr/local/lib/python3.6/site-packages/ \
  -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.6/site-packages/numpy/core/include/ \
  .. && \
  make VERBOSE=1 && \
  make && \
  make install && \
  rm -rf /opt/opencv-${OPENCV_VERSION}


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


CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]
