# BLUplaterecognition
License plate recognition

**Plan:** In an effor to do this all as elegantly as possible, with as much open source software (OSS) as possible, the 
plan is to:
1. Create an Apache OpenWhisk-incubating Docker Function (hosted on IBMCloud, known as IBMCloud Functions)
2. The user will POST an image (less than 5MB) to the endpoint
3. The function will return a JSON which will include the plate(s). 
4. This plate can be handled by the front end, which can display them all, allow user to select correct plate(s) and 
edit our best guess. 

Some issues here- 
1. we need to install OpenAPLR on an Alpine Linux based docker container.
		https://github.com/wallneradam/docker-openalpr-alpine
2. Since we have some many installs its gonna be a mess if we build this container from scratch each time.
Better to build an openwhisk docker container.  That means we have to have a wrapper fn in `action/exec`.
3. OpenALPR is _very_ poorly maintained pacakge, the python bindings are broke af.
	but it.s still best in class :'(




#### Usage

##### Docker

```bash
docker build -t openalpr https://github.com/openalpr/openalpr.git
docker run -it --rm -v $(pwd):/data:ro openalpr -c us -n 1 "test-data/s16 8319.jpg"
```

#### Dependencies

##### Apache OpenWhisk-incubating (as IBMCloud Functions) 

See (ASFv2)

To create empty docker project:
```bash
ibmcloud fn sdk install docker
```

##### OpenALPR

See https://github.com/openalpr/openalpr for info (GPLv3)

Using Python Bindings

```bash
sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
## Installer broken, simple hack here. 
sudo ln -s /usr/share/openalpr/runtime_data/ocr/tessdata/lus.traineddata /usr/share/openalpr/runtime_data/ocr/lus.traineddata
```


