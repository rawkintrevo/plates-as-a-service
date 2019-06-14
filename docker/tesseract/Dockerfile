FROM rawkintrevo/opencv-whisk
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


ENV TESSERACT_VERSION=3.05.02
# 3.05.02 builds


RUN cd /usr/local \
  && wget https://github.com/tesseract-ocr/tesseract/archive/$TESSERACT_VERSION.tar.gz \
	&& mv $TESSERACT_VERSION.tar.gz tesseract-ocr-$TESSERACT_VERSION.tar.gz \
	&& tar xf tesseract-ocr-$TESSERACT_VERSION.tar.gz \
	&& wget https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-3.02.eng.tar.gz \
	&& tar xf tesseract-ocr-3.02.eng.tar.gz \
	&& apk --no-cache add leptonica libtool \
	&& apk --no-cache add --virtual .build-deps leptonica-dev autoconf automake \
  && cd tesseract-$TESSERACT_VERSION \
  && ./autogen.sh \
	&& ./configure \
	&& make \
	&& make install \
	&& apk del .build-deps \





