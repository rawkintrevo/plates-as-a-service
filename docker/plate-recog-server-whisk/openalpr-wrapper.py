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


import sys
import subprocess
from requests import get
from json import loads
## Take command line arg 1 (json) turn it into json
## parse out args
## save image to disk

import traceback

def main():
    try:
        params = loads(sys.argv[1])
    except:
        output = {
            "msg" : "For some reason there was an error on 28...",
            'params' : sys.argv,
            "traceback" : traceback.format_tb(sys.exc_info()[2])
        }
        print(output)
        return 1


    img_url = params['url']
    print("Got url: %s" % img_url)
    n = params.get("n", 1)
    # params = {"url":"https://github.com/rawkintrevo/plates-as-a-service/raw/master/test-data/s16-8319.jpg"}
    fname = img_url.split("/")[-1]

    r = get(img_url)
    shh = open(fname, 'wb').write(r.content)
    print("Downloaded the file...")
    ## run this

    foo = subprocess.check_output(['alpr', '-n', '%i' % n, "-j", fname])
    print("ran the thing...")
    print(foo.decode().replace("\n",""))


    ## package up output

if __name__ == "__main__":
    main()

'{\"url\":', '\"https://github.com/rawkintrevo/plates-as-a-service/raw/master/test-data/s16-8319.jpg\"}'