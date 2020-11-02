FROM ubuntu:20.04

# set the base directory for signalfx
WORKDIR /signalfx

# copy source and supporting files
COPY ./signalfx_dependencies.txt ./signalfx_post_event.py ./signalfx_start_service.sh ./

# required to install base dependencies
RUN apt-get -y update

# install base dependencies
RUN apt-get install -y python3.8 python3.8-distutils
RUN apt-get install -y python3-pip

# install signalfx service dependencies
RUN pip3 install -r signalfx_dependencies.txt

# set the listerner port for signalfx service
EXPOSE 4996

# set the file perms to executable
RUN chmod +x signalfx_start_service.sh

# entry point for signalfx service
CMD ["./signalfx_start_service.sh"]