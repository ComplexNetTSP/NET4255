# NET 4251: High Availability Web Service

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu), [Hossam Afifi](mailto:hossam.afifi@telecom-sudparis.eu) 

* Firstname: XXXXX 
* Lastname: XXXXX

## Introduction
* Clone this repository
* Each challenge **must be validated** with a professor and then committed and pushed to your own github repository.
* Before starting a given step, present the sketch of your infrastructure to a professor.
* We strongly recommend that you use [Alpine OS](https://www.alpinelinux.org/) as the base operating system for your [docker](https://www.docker.com/blog/how-to-use-the-alpine-docker-official-image/). 

## Challenge 0: Install 
On your onwn computer install the following softwares:
* [Docker Desktop](https://docs.docker.com/get-docker/)
* [Conda](https://www.anaconda.com/download)
* IDE ([VSCode](https://code.visualstudio.com/), etc)

## Challenge 1: Create a Simple Web page and develop a docker file for your website (2 pts)

* Build a one page Flask application which contains of following elements:
  * your name
  * your projet name
  * the version of your website (i.e. V1)
  * the server hostname
  * the current date
* Build a docker container which contain your Flask web page
* Test your application
* Send your docker container on [DockerHub](https://hub.docker.com/})
* Draw a schema of your systems (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address
  * Show the container ports 

### References 
* [Getting started with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [Containerize an application](https://docs.docker.com/get-started/02_our_app/)

## Challenge 2: Create docker compose to deploy a mongodb database server (2pts)
* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [mongodb community server](https://hub.docker.com/r/mongodb/mongodb-community-server))
* Use docker compose to deploy your mongodb database
* Test your application and add record in your database manualy with the mongod command ([see the install requirement for mongodb](https://www.mongodb.com/docs/v3.0/tutorial/install-mongodb-on-windows/)
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the containers IP address or hostname
  * Show the container ports 

## Challenge 3: Create docker compose file to deploy a simple web service (flask + mongodb) (3pts) 
* Update your Flask application and add the following items:
  * your name
  * your projet name
  * the version of your website (i.e. V2)
  * the server hostname
  * the current date
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
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address
  * Show the container ports 

### References 
* [Docker compose gettig started](https://docs.docker.com/compose/gettingstarted/)
* [Configure the default network](https://docs.docker.com/compose/networking/)
* [How to get the last N records in mongodb?](https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb)

## Challenge 4: Install a load balancer for your infrastructure (2pts)

Add a [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) load balancer to your Docker compose file. Update your docker compose file with the following elements:
* 2 Flask application
  * Deploy 1 Flask app without dabase connexions
  * Deploy 1 Flask app with database connexions
* 1 NGINX load balancer which load balance the load between the two web server
* 1 mongodb database
* Network
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 
  
### References 
* [Sample Load balancing solution with Docker and Nginx](https://towardsdatascience.com/sample-load-balancing-solution-with-docker-and-nginx-cf1ffc60e644)
* [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)

## Challenge 5: Learn Kubernetes with the online tutoral (2pts)
* Ask the professor to get access to the Kubernetes server: register your Telecom SudParis email (firstname.lastname@telecom-sudparis.eu) as a valide google address.
* Install [gcloud cli](https://cloud.google.com/sdk/docs/install?hl=fr#linux)
* Install [kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=fr#gcloud)
* Install the kubeconfig file on your computer

```bash
> gcloud container clusters get-credentials net4251 --region=us-central1
```

after this command your should have kubeconfig.yml file on your laptop. This file will enable you to get access to the kubernetes cluster.

```bash
> ls $HOME/.kube/
kubeconfig.yml
```

Check the following command in order to check the connexion. You sould see a namespace with your name !!!

```bash
> kubectl get namespace
```

* Follow the [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)

### References
* [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)
  
## challenge 6: Lauch your first Pod in command line (1pts)
Create your first deployemnt in command lien with the **kubectl** command: 
* Create a deployment for the webnodb container in your own namespace
   * without any replicat
   * without **any service**
* Check that your deployment is sucessfull

### Refernces
* 
## challenge 7: Create your first deployement file with a clusterIP service (1pts)
* Create a deployenment file for your container **without database**
* becarful, create your deployment in your on namespace 
* Create a schema to explain how a request is served to the pod (i.e. a pod):
  * the schema should explain wich port is used at each step and what IP address is used by each componenent (nodes, pods, services)
* connect to the cluster through a proxy with teh foillowing command:

```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001 
```
now your can access to the **webnodb** web page at the following url 
27.0.0.1:8001/api/v1/namespaces/**your namespace name**/services/** your service name**/proxy/

### References
* [Kubernetes YAML File Explained - Deployment and Service](https://youtu.be/qmDzcu5uY1I?si=jeoMTcyKxxQ70jmG)
* [Accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/)
* [Manually constructing apiserver proxy URLs](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/#manually-constructing-apiserver-proxy-urls)
  
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
