# BLUplaterecognition
License plate recognition

We use an Apache OpenWhisk-incubating docker function loaded with OpenALPR to detect plates.

#### Usage

##### Docker

In `docker/` you will see directories cooresponding to various docker build stages:

- `dockerSkelaton` is the base image for OpenWhisk Functions
- `opencv` 
- `tesseract`
- `openalpr`

It is worth noting that there is a lot of liposuction opportunity on these fatty-bo-batty containers.

#### Dependencies

##### Apache OpenWhisk-incubating (as IBMCloud Functions) 

See (ASFv2)

To create empty docker project:
```bash
ibmcloud fn sdk install docker
```

##### OpenALPR

S
