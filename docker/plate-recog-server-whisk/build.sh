#!/usr/bin/env bash

VERSION=0.0.14
docker build -t rawkintrevo/plate-recog-server-whisk:$VERSION .
docker push rawkintrevo/plate-recog-server-whisk:$VERSION
docker run -it rawkintrevo/plate-recog-server-whisk:$VERSION /action/exec '{"url":"https://raw.githubusercontent.com/rawkintrevo/plates-as-a-service/master/test-data/s16-8319.jpg"}'
ibmcloud fn action delete blu/test
ibmcloud fn action create blu/plate-recog --docker rawkintrevo/plate-recog-server-whisk:$VERSION
ibmcloud fn action invoke --blocking --result blu/plate-recog --param url "https://github.com/rawkintrevo/plates-as-a-service/raw/master/test-data/s16-8319.jpg"