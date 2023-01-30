# High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu)


## Introduction

* Each step should be validated with a professor
* You should maintain a gitlab/github repository for your project
* Before starting a given step present the sketch of your infrastructure to a professor

## Develop a docker file for your website

* Build a one page web page with Flask which state:
  * your name
  * your projet name
  * The version of your website (i.e. V1)
  * The current date
* Build a docker container which contain your Flask web page
* Test your application
* Send your docker container on [DockerHub](https://hub.docker.com/})

### References 
* [Getting started with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [Containerize an application](https://docs.docker.com/get-started/02_our_app/)

## Compose a simple web service (flask + mongodb) with docker compose

* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [official mongodb docker](https://hub.docker.com/_/mongo))
* Create a docker compose file with the following elements:
  * Docker service for your website 
  * Docker service for your mongodb database
  * Network

### References 
* [Docker compose gettig started](https://docs.docker.com/compose/gettingstarted/)

## Install a load balancer for your infrastructure

## Test your infrastructure with Minikube

## Deploy your infrastructure with kubernetes

## Automates your deployment with Ansible

## Enable autoscaling with kubernetes

## Create a new version of your website and deploy it with an rolling update

## Collect build a docker container to collect all the log
