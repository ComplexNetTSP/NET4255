# High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu)


## Introduction
* You should maintain a github repository for your project
* Each step should be validated with a professor and then commited and push on github
* Before starting a given step present the sketch of your infrastructure to a professor

## 1. Develop a docker file for your website

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

## 3. Compose a simple web service (flask + mongodb) with docker compose

* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [official mongodb docker](https://hub.docker.com/_/mongo))
* Update Flask application such that:
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

## Install a load balancer for your infrastructure

Add a [Traefik](https://doc.traefik.io/traefik/) load balancer to your Docker compose file. Update your docker compose file with the following elements:
* [Traefik load balancer](https://doc.traefik.io/traefik/)
* Two Docker service with your Flask application  
* Docker service for your mongodb database
* Network

### References 
* [Traefik](https://doc.traefik.io/traefik/)
* [Traefik Quick Start](https://doc.traefik.io/traefik/getting-started/quick-start/)

## Test your infrastructure with Minikube

### References
* [From Docker Compose to Minikube](https://medium.com/skillshare-team/from-docker-compose-to-minikube-d94cbe97acda)

## Deploy your infrastructure with kubernetes

## Automates your deployment with Ansible

## Enable autoscaling with kubernetes

## Create a new version of your website and deploy it with an rolling update

## Collect build a docker container to collect all the log
