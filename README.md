# NET 4251: High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu), [Hossam Afifi](mailto:hossam.afifi@telecom-sudparis.eu) 

* Firstname: XXXXX 
* Lastname: XXXXX

## Introduction
* Clone this repository
* Each Challenge **must be** validated with a professor and then commited and push to your own github repository
* Before starting a given step present the sketch of your infrastructure to a professor

## Challenge 0: Install 
On your onwn computer install the following software:
* [Docker Desktop](https://docs.docker.com/get-docker/)
* [Conda](https://www.anaconda.com/download)
* IDE ([VSCode](https://code.visualstudio.com/), etc)

## Challenge 1: Create a Simple Web page and develop a docker file for your website (2 pts)

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

## Challenge 2: Create docker compose to deploy a mongodb database server 
* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [official mongodb docker](https://hub.docker.com/_/mongo))
* Use docker compose to deploy your mongodb database
* Test your application and add record in your database manualy with the mongod command ([see the install requirement for mongodb](https://www.mongodb.com/docs/v3.0/tutorial/install-mongodb-on-windows/)

## Challenge 3: Create docker compose file to deploy a simple web service (flask + mongodb) 
* Update your Flask application and add the following items:
  * your name
  * your projet name
  * The version of your website (i.e. V2)
  * The machine hostname
  * The current date
* Flask apllication should connect to a mongodb database each time a request is served :
  * It connect to the mongodb database through [pymongo](https://pymongo.readthedocs.io/en/stable/)
  * For each request, it will record in the mongodb database:
    * the ip address of the client
    * the current date
* your flask application should display the last 10 records of the database
* Update Fask app version displayed on the page to V2
* Finaly deploy your services using a docker compose file with the following elements:
  * Docker service for your website (you flask application)
  * Docker service for your mongodb database
  * Network to connect the previous services 

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

## Challenge 11: Deploy with HELM a service of your choice 
* create a a master slave architecture with mongodb 
