

# NET 4255: High Availability Web Services

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
</p>

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu), [Hossam Afifi](mailto:hossam.afifi@telecom-sudparis.eu) 

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

## Challenge 5: Learn Kubernetes with the online tutoral (1pts)
* Ask the professor to get access to the Kubernetes server: register your Telecom SudParis email (firstname.lastname@telecom-sudparis.eu) as a valide google address or provide valide gmail address.
* Install [gcloud cli](https://cloud.google.com/sdk/docs/install?hl=fr#linux)
* Install [kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=fr#gcloud)
* you should have access to the cluster dashboard at the following address: [https://console.cloud.google.com/kubernetes](https://console.cloud.google.com/kubernetes)
* login with gcloud 
```bash
$ gcloud auth login 
...
```

* Select net4251 as the default project 
```bash
$ gcloud config set project net-4251 
```
* Install the kubeconfig file on your computer

```bash
$ gcloud container clusters get-credentials net4251-kube-cluster --region=us-central1
```

after this command your should have kubeconfig.yml file on your laptop. This file will enable you to get access to the kubernetes cluster.

```bash
> ls $HOME/.kube/
kubeconfig.yml
```

Export kubeconfig file  
```bash
export KUBECONFIG=$HOME/.kube/kubeconfig.yml
```

Now, you should be able to connect to the kuberntest cluster. Check the following command in order to check the connexion. 
```bash
$ kubectl cluster-info
...
```

You sould see a namespace with your name !!! with the following command:
```bash
$ kubectl get namespace
```

* Follow the [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)

### References
* [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)
  
## Challenge 6: Lauch your first Pod in command line (1pts)
Create your first deployemnt in command line with the **kubectl** command: 
* Create a deployment for the webnodb container in your own namespace
   * without any replicat
   * without **any service**
* Check that your deployment is sucessfull in the [google cloud console](https://console.cloud.google.com/kubernetes/) and with the command line: 
```bash 
$ kubectl get deployments -o wide
...
$ kubectl get pods -o wide
...
```

* Test the pod web server id correctly running with port-forwarding 
```bash
kubectl port-forward pods/xxxx your pod name xxxx :xxx pod port xxx --namespace=xxxx your namespace xxxx
Forwarding from 127.0.0.1:54127 -> 5000
```
Now you can connect to with yoru browser to `http://127.0.0.1:54127` to access the webnodb website.


### References
* [Deploying your first app on Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
* [Utiliser le Port Forwarding pour accéder à des applications dans un cluster](https://kubernetes.io/fr/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)

## Challenge 7: Create your first deployement file with a NodePort service (1pts)
* Create a Deployment file for your container webnodb (**the one without database**)
* Becareful, create your **Deployment** and **the NodePort service** in your on namespace !!!!
* show on a new schema how a request is served from the service to the pods:
  * the schema should explain wich port is used at each step and what IP address is used by each componenent (nodes, pods, services)
* connect to the cluster through a proxy with the following command or use port-forwarding to test your application:

```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001 
```

Now should be able to access to the **webnodb** web page at the following url: 
* `http://127.0.0.1:8001/api/v1/namespaces/__your_namespace_name__/services/__your_service_name__/proxy/`
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References
* [Kubernetes YAML File Explained - Deployment and Service](https://youtu.be/qmDzcu5uY1I?si=jeoMTcyKxxQ70jmG)
* [Accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/)
* [Manually constructing apiserver proxy URLs](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/#manually-constructing-apiserver-proxy-urls)
  
## Challenge 8: Deploy on the Kubernetes cluster your website (webdb) and the respective mongodb database (2pts)

* Deploy the webdb web service with 3 replica and its related service (**NodePort**)
* Deploy the mongodb database and its related service (**ClusterIP**)
* Connect the web service to teh database using kubernetes DNS hostname
* Explain the difference between a NodePort Service and a ClusterIP service
* Validate your deployment (webdb, mongodb) by using port-forwarding 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References 
* [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)

## Challenge 9: Expose your services (1pts)
* Create a Ingress in order to expose your web application (webnodb and webdb)
  * GKE has some custom made feature in order to deploy Ingress, be sure to read carefully to Ingress documenation of [GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress?hl=fr)
  * Don't forget to deploy your ingress in your own namespace !!!
* The kubenetes cluster has a public IP address with the hostname: "net4251.luxbulb.org" create a service that redirect http traffic of the following url to your respective deployement: 
  * url 1: http://webnodb.your_name.net4251.luxbulb.org/ => deployement webnodb
  * url 2: http://webdb.your_name.net4251.luxbulb.org/ => deployement webdb
* Test your Ingress 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

**Warning, please call the teacher before applying your Ingress.**

### References
* [GKE ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress?hl=fr)

## Challenge 10: Automate your deployement with HELM (1pts)
* Create a HELM Chart to deploy the whole infrastructure 
* Use ConfigMaps to store database hostname and port information
* Use Secrets to store the database credentials

## Challenge 11: Horizontal Scalling and Vertical Scaling 

## Challenge 12: Create a Network policy 
* Create a Network policy that restrict the access to to database only to IP address corresponding to your Web Pods 

## Challenge 13: Create a distributed database system
* Create a a master slave architecture with mongodb 
* create a pvc to store the database 
* create a headless service 
* update the your application to read from all the database in rod nroungin way but write to master

### References
* [Replication Introduction](https://www.mongodb.com/docs/v2.4/core/replication-introduction/)
* [Deploy a Replica Set](https://www.mongodb.com/docs/v2.4/tutorial/deploy-replica-set/)
* [Kubernetes StatefulSet explained](https://youtu.be/pPQKAR1pA9U?si=pjmaqy5EvE3P4W2c)
* [Statefulsets | Deploying MongoDB cluster to Kubernetes](https://youtu.be/eUa-IDPGL-Q?si=wcZc2AVhYXit0OSD)

## Challenge 14: Deploy with HELM a service of your choice 
