# High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu), [Hossam Afifi](mailto:hossam.afifi@telecom-sudparis.eu) 

Firstname: XXXXX 
Lastname: XXXXX

## Introduction
* Clone this repository
* Each Challenge **must be** validated with a professor and then commited and push to your own github repository
* Before starting a given step present the sketch of your infrastructure to a professor

## Challenge 0: Install 
On your onwn computer install the following software:
* Docker Desktop
* IDE (VSCode, etc)

## Challenge 1: Create a Simple Web page and develop a docker file for your website

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

## Challenge 2: Build a docker file to host a database server 

* Build a one page Flask application which contains of following elements:
  * your name
  * your projet name
  * The version of your website (i.e. V2)
  * The machine hostname
  * The current date
 
* Build a docker 
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

## Challenge 5: Learn Kubernetes with the online tutoral 
* Ask the professor to get access to the Kubernetes server: register your Telecom SudParis email (firstname.lastname@telecom-sudparis.eu) as a valide google address.

### References
* https://kubernetes.io/docs/tutorials/
  
## challenge 6: Deploy your infrastructure with kubernetes without DB
* Deployenment and services without database
* Autocaling
* Minumum of 3 servers 

## challenge 7: Deploy your infrastructure with kubernetes without DB
* Deployenment with ingress without database
* Create a schema to explain how a request is served by a docker container (i.e. a pod):
  * the schema should explain wich port is used at each step and what IP address is used by each componenent
 
## challenge 7: Deploy your infrastructure with kubernetes and with DB 
* don't use helm to deploy your database 

## Challenge 8: Automate your deployement with HELM

## Challenge 9: Create a Network policy 
* Goal restrict the access to to database only to IP address corresponding to your Web Pod 

## Challenge 9: Create a Network policy 
* Goal restrict the access to to database only to IP address corresponding to your Web Pod 

## Challenge 10: Create a distributed database system
* create a a master slave architecture with mongodb 


