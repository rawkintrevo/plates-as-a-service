

import subprocess

## Take command line arg 1 (json) turn it into json
## parse out args
## save image to disk

## run this
foo = subprocess.check_output(['alpr', '-n', '1', 'test-data/s16-8319.jpg'])

## package up output