FROM rawkintrevo/tesseract-whisk
#Licensed to the Apache Software Foundation (ASF) under one
#or more contributor license agreements.  See the NOTICE file
#distributed with this work for additional information
#regarding copyright ownership.  The ASF licenses this file
#to you under the Apache License, Version 2.0 (the
#"License"); you may not use this file except in compliance
#with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied.  See the License for the
#specific language governing permissions and limitations
#under the License.


ENV CC /usr/bin/gcc
ENV CXX /usr/bin/g++

RUN \
    # Enable testing repo
    echo "http://nl.alpinelinux.org/alpine/edge/testing" >>/etc/apk/repositories \
    && apk update && apk upgrade \
    && cat /etc/apk/repositories \
    # Install needed libs
    && echo "Installing required libs" \
    && apk add curl-dev log4cplus log4cplus-dev g++ libexecinfo libexecinfo-dev \
    && apk --no-cache add \
       libcanberra-gtk3 ttf-freefont \
    # Install build dependencies
    && apk --no-cache add --virtual .build-deps \
       ca-certificates wget \
       git gcc g++ cmake make curl-dev log4cplus-dev   bzip2-dev libc-dev \
       # opencv-dev
    # Prepare build directories
    && cd /srv \
    && git clone https://github.com/openalpr/openalpr.git \
    && cd openalpr/src && mkdir build && cd build \
    # Patch to be able to compile with Musl glibc
    && echo "doing the thing on daemon.cpp---------------------------------------------------------------------------" \
    && sed -i.bak 's/backtrace/0;\/\//' /srv/openalpr/src/daemon.cpp \
    && echo "it's done" \
    # Build
    && cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc .. && \
       make -j8 && \
       make install \
    # Clean not needed build directory and dependencies
    && rm -rf /srv/openalpr \
    && apk del .build-deps \
    # Create working directory
    && mkdir /openalpr

