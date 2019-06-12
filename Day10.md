# Day 10

*   There is a command in linux which reverse the lines order in cat command, the command is ```tac```.
```
tac Day1.md
```
*   There is a command to reverse the string characters in a line ```rev``` is a command we can use.
```
rev Day1.md
```
*   To generate qr code in shell we have a package called ```qrencode```
```
qrencode -s 32x32 -o akshayimage.png
http://www.akshaybengani.github.io
```
## Docker
*   It is a technology which provide us platform to do multiple type of things in a single platform or a system.
*   Docker is a platform provider.
*   We can use Docker to provide enviorment for website, Apps, Console applications etc.
*   Docker can be used to build hadoop platform.
*   It is a platform which can run on any platform.
*   Docker uses your base OS Kernel to build new operating systems. 
*   It means if you have windows as your base system on which docker is installed, then Windows NT kernel will be used to build new OS in Docker.
*   Windows Server 2016 supports Docker support.
*   Docker is developed in Go which is a superfast language.

## Install Shellinabox
*   It is a program which allows us to use shell in our browser insteed of a ssh or a putty.
*   
*   

## Docker Basics
*   To install a OS in docker we need a docker-image.
*   You can explore docker-images online on https://www.hub.docker.com
*   To search a docker image we have a command ```docker search java```
*   To download a image from docker liberary we use a command ```docker pull```
```
docker pull hello-world
docker pull python
docker pull fedora
```
```
[root@ip-172-31-9-238 ~]# docker pull fedora
Using default tag: latest
Trying to pull repository docker.io/library/fedora ...
latest: Pulling from docker.io/library/fedora
8f6ac7ed4a91: Pull complete
Digest: sha256:9c78c69f748953ba8fdb6eb9982e1abefe281d9b931a13f251eb8aec988353de
Status: Downloaded newer image for docker.io/fedora:latest
```
*   To check how many images we have installed on docker we have a command ```docker images```
```
[root@ip-172-31-9-238 ~]# docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
docker.io/python        latest              34a518642c76        28 hours ago        929 MB
docker.io/fedora        latest              289289d1a15b        30 hours ago        318 MB
docker.io/hello-world   latest              fce289e99eb9        5 months ago        1.84 kB
```
*   We can make container from any image.
*   To build a OS from docker we have a command called ```docker run```
```
docker run -it fedora date
```
*   ```i``` stands here for interactive
*   ```t``` stands here for terminal
*   ```date``` stands here for the application program date.
*   To know how many docker containers exist in current time either in shutdown or running we have a command called ```docker ps -a```
*   Docker is a process maintainer it can run that single process only.
*   If we want container not to stop then we can open a program ```bash```.
```
[ec2-user@ip-172-31-9-238 /]$ sudo docker run -it fedora bash
[root@ef3271f6d299 /]#
```
*   To start an existing container we have a command ```docker start``` with the container name and you can get the container name using ```docker ps -a```
```
docker start blissful_blackwell
```
*   To view the running containers we have a command ```docker ps``` this will give list of running containers.
*   To use the container we have already created or shutdown container we have a command called ```docker attach CONTAINER_NAME```
```
docker start gracious_borg
docker attach gracious_borg
```
*   First we need to start the shutdowned container then we can attach the existing container.
*   To delete a conatiner we have a command ```docker container rm CONTAINER_ID```
*   To list all the containers we have a command
```
docker container ls -a
```
*   Full form of ```ps``` is ```Process Status```
*   To give a custom name to the container we can use the attribute --name and assign the name of the container.
```
docker run -it --name akshayc1 fedora bash
```
*  It is not important that there are all basic packages of linux installed in the image.
*   To run a docker image without exiting at the exit code use the command ```exec```.
```
docker exec -it Akshayc1 bash
``` 
*   We can use internet in docker container also install ping using yum
*   ping command includes in iputils
*   To delete an image from docker liberary we have command ```docker rmi DOCKER_IMAGE_```
```
docker rmi docker.io/python
```
*   To delete a container we use ```docker rm CONTAINER_ID``` 
```
docker rm 3346e5f5280c
```
*   To delete all the containers in one run
```
docker rm $(docker ps -qa)
```
*    To create n number of docker containers we can use shell scripting loop
```
for((i=1;i<100;i++))
do
docker run fedora
done
```
*   To get the continer IP use this command
```
docker inspect CONTAINER_NAME | grep -i ipadd
```