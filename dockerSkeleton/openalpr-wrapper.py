
import sys
import subprocess
from requests import get
from json import loads
## Take command line arg 1 (json) turn it into json
## parse out args
## save image to disk


params = loads(sys.argv[1])
img_url = params['url']
n = params.get("n", 1)
# {"url":"https://github.com/rawkintrevo/plates-as-a-service/raw/master/test-data/s16-8319.jpg"}
fname = img_url.split("/")[-1]

r = get(img_url)
open(fname, 'wb').write(r.content)

## run this
foo = subprocess.check_output(['alpr', '-n', '1', "-j", fname])
print(foo)
## package up output