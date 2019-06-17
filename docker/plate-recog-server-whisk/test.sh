#!/usr/bin/env bash

docker run -it rawkintrevo/plate-recog-server-whisk /action/exec '{"url":"https://raw.githubusercontent.com/rawkintrevo/plates-as-a-service/master/test-data/s16-8319.jpg"}'
