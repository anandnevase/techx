#TechX Calculator

TechX Calculator. For Demo
=========================================
Then you can run AMF Xporter app

    $ calculator


To run tests, do the following from source root

    $ ./run-tests.sh

If you need to run TechX Calculator in a docker environment, please read the following topics.

Installing Docker
=================

Install docker on [Windows, Mac OS X, or Linux](https://docs.docker.com/installation/)

Build TechX Calculator Docker Image
==============================

Run the following command from the source code root directory (make sure that you are running the command from
Docker Quickstart Terminal):

    $ ./build-docker-image.sh

 Once the build is over you could see the new image using the following command

    $ docker images
    REPOSITORY                     TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
    calculator                    lagesh                 sha256:c3e80        19 hours ago        132.6 MB

Run  TechX Calculator Application
===========================

Execute following command to run AMF-Xporter application:

    $ docker run --net=host -it anandnevase/calculator

To get the docker host IP, run

    $ docker-machine ip default
    192.168.99.100

And goto [http://192.168.99.100:8080](http://192.168.99.100:8080) to see the application in action.