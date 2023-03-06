# High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu)


## Introduction
* You should maintain a github repository for your project
* Each step should be validated with a professor and then commited and push on github
* Before starting a given step present the sketch of your infrastructure to a professor

## Challenge 1: Develop a docker file for your website

* Build a one page Flask application which contains of following elements:
  * your name
  * your projet name
  * The version of your website (i.e. V1)
  * The machine hostname
  * The current date
* Build a docker container which contain your Flask web page
* Test your application
* Send your docker container on [DockerHub](https://hub.docker.com/})

### References 
* [Getting started with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [Containerize an application](https://docs.docker.com/get-started/02_our_app/)

## Challenge 2: Develop a docker file for your website with a databse 

* Build a one page Flask application which contains of following elements:
  * your name
  * your projet name
  * The version of your website (i.e. V2)
  * The machine hostname
  * The current date
  * A connexion to a mongo database:
     * store in the db: current date, ip, page url for each requesting http-get 
     * display the database content in the webpage 
* Build a docker container which contain your Flask web page
* Test your application
* Send your docker container on [DockerHub](https://hub.docker.com/})


## Challenge 3: Compose a simple web service (flask + mongodb) with docker compose

* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [official mongodb docker](https://hub.docker.com/_/mongo))
* Use the previous docker file to create a docker compose with the following items:
  * It connect to the mongodb database (use [pymongo](https://pymongo.readthedocs.io/en/stable/))
  * For each request, it will record in the mongodb database: the ip address of the client and the current date
  * It display the last 10 records of the database
  * Update Fask app versiion displayed on the page to V2 
* Create a docker compose file with the following elements:
  * Docker service for your website 
  * Docker service for your mongodb database
  * Network

### References 
* [Docker compose gettig started](https://docs.docker.com/compose/gettingstarted/)
* [Configure the default network](https://docs.docker.com/compose/networking/)
* [How to get the last N records in mongodb?](https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb)

## Challenge 4: Install a load balancer for your infrastructure

Add a [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) load balancer to your Docker compose file. Update your docker compose file with the following elements:
* Two Docker service with your Flask application  
* Docker service for your mongodb database
* Network
* deploy 2 docker of your website without db connexions
* deploy 2 docker of your website with db connexions

### References 
Put references here

## challenge 5: Deploy your infrastructure with kubernetes without DB

### 1. Perform the kubernetes tutorial either localy with minikube or with the help of the online tutorial

### 2. Next step on the kubernetes server 
Deploy with kubernetes command line the following items:
* deployment of your website without db backend 
* create a service to link the deployment  

### References
* https://kubernetes.io/docs/tutorials/


## Challenge 6: Create a Ingress file (NGINX)

## Challenge 7: Deploy your infrastructure with kubernetes with DB 

## Challenge 8: Automate your deployement with HELM


