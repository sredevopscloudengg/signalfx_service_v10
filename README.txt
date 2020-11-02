# SignalFx Service Rest End Point: Requirements
1) Correctly accept a POST request from our internal health service
2) Correctly POST a new event to SignalFX (https://developers.signalfx.com/ingest_data_reference.html)
3) Run as a Docker container
4) We like tests, so should you
  Your project will need to provide a build tool (Bash, Makefile, etc) to do the following:
  docker: build the container
  docker-run: build the container and run the service
  docker-shell: build the container and run a shell inside it
  docker-test: build the container and run any test suite you have
 
# SignalFx Service Rest End Point Project Files: Notes
1) signalfx_build.sh
signalfx_build.sh is the make file for this project. 
It creates a docker image, container, starts the container and starts the signalfx service.
signalfx service is configured to run at port 4996 on the container and on the host.
2) signalfx_post_event.py
signalfx_post_event.py is the source file for the signalfx rest endpoint.
This uses the vanilla flask microservice framework to build the rest endpoint.
3) signalfx_start_service.sh
signalfx_start_service.sh is the entrypoint for the signalfx rest endpoint in the Dockerfile.
4) signalfx_unit_test.py
signalfx_unit_test.py is the unit test file for the signalfx rest endpoint.
5) signalfx_dependencies.txt
signalfx_dependencies.txt contains the required libraries for the signalfx rest endpoint.
6) Dockerfile
Dockerfile is the base template to build the docker image for the signalfx rest endpoint.

# SignalFx Service Rest End Point: Instructions
1) On the windows machine, run the make file "./signalfx_build.sh"
   On the linux machine, change the following lines and then run the make file ./signalfx_build.sh. 
   Comment the line below in the file "signalfx_build.sh"
   -------------> winpty docker run -p 4996:4996 -d $IMAGE_NAME
   UnComment the line below in the file "signalfx_build.sh"
   -------------> docker run -p 4996:4996 -d $IMAGE_NAME
2) run the command "docker images" and check for "signalfx" under the column "REPOSITORY" .
3) run the command "docker ps" and check for "signalfx" under the column "IMAGE".
4) run the signalfx_unit_test.py to run unit tests.
5) run the command below to run smoke tests.
curl -H "Content-Type: application/json" -X POST -d '{"id":"i-0085adkdfjkj2895", "description":"This server is unhealthy"}' http://127.0.0.1:4996/

# SignalFx Service Rest End Point: Exceptions
1) This project was designed on the windows machine
2) Some docker commands such as below will not work without appending "winpty"
   winpty docker run -p 4996:4996 -d $IMAGE_NAME
3) I am using trail version of the signalfx cloud service which is only valid for 10 days.
   Please refer to the line numbers #38-42 in the file signalfx_post_event.py to replace the "ORG_TOKEN" and the "ingest_endpoint" with a non-trail version.
