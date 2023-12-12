
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
</p>

<h1 align="center">NET 4255: High Availability Web Services</h1>

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu)
### Assistant: [Gatien Roujanski](mailto:gatien.roujanski@telecom-sudparis.eu) 

## Introduction
* Clone this repository
* Each challenge **must be validated** with a professor and then committed and pushed to your own github repository.
* Before starting a given step, present the sketch of your infrastructure to a professor.
* We strongly recommend that you use [Alpine OS](https://www.alpinelinux.org/) as the base operating system for your [docker image](https://www.docker.com/blog/how-to-use-the-alpine-docker-official-image/). 

## Challenge 0: Install 
On your own computer install the following software:
* [Docker Desktop](https://docs.docker.com/get-docker/)
* [Conda](https://www.anaconda.com/download)
* IDE ([VSCode](https://code.visualstudio.com/), etc)

## Challenge 1: Create a Simple Web page and develop a docker file for your website (2 pts)

* Build a one page Flask application which contains the following elements:
  * Your name
  * Your project name
  * Version of your website (i.e. V1)
  * The server hostname
  * The current date
* Build a docker container which contains your Flask web page
* Test your application
* Send your docker container on [DockerHub](https://hub.docker.com/})
* Draw a schema of your systems (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address
  * Show the container ports
 
### Notes about Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. 

A minimal Flask application looks something like this:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Now you can run the web serveur you just created

```bash
$ flask --app hello run
* Serving Flask app 'hello'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

See the [quickstart guide](https://flask.palletsprojects.com/en/3.0.x/quickstart/) for more information

### References 
* [Getting started with Flask](https://fflask.palletsprojects.com/en/3.0.x/quickstart/)
* [Containerize application](https://docs.docker.com/get-started/02_our_app/)

## Challenge 2: Create docker compose to deploy a mongodb database server (2pts)
* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [mongodb community server](https://hub.docker.com/r/mongodb/mongodb-community-server))
* Use docker compose to deploy your mongodb database
* Test your application and add record in your database manually with the mongod command ([see the install requirement for mongodb](https://www.mongodb.com/docs/v3.0/tutorial/install-mongodb-on-windows/)
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the containers IP address or hostname
  * Show the container ports
 
### References 
* [Docker compose gettig started](https://docs.docker.com/compose/gettingstarted/)

### Why mongodb ?
MongoDB is a database based on nosql. It's easier to create a master/slave database cluster when using nosql. 

## Challenge 3: Create docker compose file to deploy a simple web service (flask + mongodb) (2pts) 
* Update your Flask application and add the following items:
  * Your name
  * Your project name
  * Version of your website (i.e. V1)
  * The server hostname
  * The current date
* Flask application should connect to a mongodb database each time a request is served :
  * It connects to the mongodb database through [pymongo](https://pymongo.readthedocs.io/en/stable/)
  * For each request, it will record in the mongodb database:
    * The IP address of the client
    * The current date
* Your flask application should display the last 10 records of the database
* Update Flask app version displayed on the page to V2
* Finaly deploy your services using a docker compose file with the following elements:
  * Docker service for your website (your flask application)
  * Docker service for your mongodb database
  * Network to connect the previous services
* Send your docker container on [DockerHub](https://hub.docker.com/}) with the correct tags.
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address
  * Show the container ports 

### References 
* [Docker compose gettig started](https://docs.docker.com/compose/gettingstarted/)
* [Configure the default network](https://docs.docker.com/compose/networking/)
* [How to get the last N records in mongodb?](https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb)

## Challenge 4: Install a load balancer for your infrastructure (1pts)

Add a [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) load balancer to your Docker compose file. Update your docker compose file with the following elements:
* 2 Flask application
  * Deploy 1 Flask app without database connections
  * Deploy 1 Flask app with database connections
* 1 NGINX load balancer which balances the load between the two web server
* 1 Mongodb database
* Network
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 
  
### References 
* [Sample Load balancing solution with Docker and Nginx](https://towardsdatascience.com/sample-load-balancing-solution-with-docker-and-nginx-cf1ffc60e644)
* [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)

## Challenge 5: Learn Kubernetes with the online tutorial (1pts)
* Ask the professor to get access to the Kubernetes server: register your Telecom SudParis email (firstname.lastname@telecom-sudparis.eu) as a valid google address or provide valid gmail address (name@gmail.com).
* Install [gcloud cli](https://cloud.google.com/sdk/docs/install?hl=fr#linux)
* Install [kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=fr#gcloud)
* You should have access to the cluster dashboard at the following address: [https://console.cloud.google.com/kubernetes](https://console.cloud.google.com/kubernetes)
* Login with gcloud 
```bash
$ gcloud auth login 
...
```

* Select net-4255 as the default project 
```bash
$ gcloud config set project net-4255 
```
* Install the kubeconfig file on your computer

```bash
$ gcloud container clusters get-credentials net4255-gke --location=us-central1-a
```

After this command you should have kubeconfig.yml file on your laptop. This file will enable you to get access to the kubernetes cluster.

```bash
$ ls $HOME/.kube/
kubeconfig.yml
```

Export kubeconfig file  
```bash
$ export KUBECONFIG=$HOME/.kube/kubeconfig.yml
```

Now, you should be able to connect to the kuberntest cluster. Check the following command in order to check the connection. 
```bash
$ kubectl cluster-info
...
```

You should see a namespace with your name !!! with the following command:
```bash
$ kubectl get namespace
```

* Follow the [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)

### References
* [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)
  
## Challenge 6: Launch your first Pod in command line (1pts)
Create your first deployment in command line with the **kubectl** command: 
* Create a deployment for the webnodb container in your own namespace
   * Without any replicat
   * Without **any service**
* Check that your deployment is successful in the [google cloud console](https://console.cloud.google.com/kubernetes/) and with the command line: 
```bash 
$ kubectl get deployments -o wide
...
$ kubectl get pods -o wide
...
```

* Test the pod web server id correctly running with port-forwarding 
```bash
$ kubectl port-forward pods/xxxx your pod name xxxx :xxx pod port xxx --namespace=xxxx your namespace xxxx
Forwarding from 127.0.0.1:54127 -> 5000
```
Now you can connect with your browser to `http://127.0.0.1:54127` to access the webnodb website.


### References
* [Deploying your first app on Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
* [Utiliser le Port Forwarding pour accéder à des applications dans un cluster](https://kubernetes.io/fr/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)

## Challenge 7: Create your first deployment file with a ClusterIP service (1pts)
* Create a Deployment file for your container webnodb (**the one without database**)
* Be careful, create your **Deployment** and **the ClusterIP service** in your on namespace !!!!
* Show on a new schema how a request is served from the service to the pods:
  * The schema should explain which port is used at each step and what IP address is used by each component (nodes, pods, services)
* Request the following resources per pod:
  * cpu resource: 1/10 CPU per pod 
  * memory: 100 Mo per pod
* Limit your pod resources as the following:
  * cpu resourse: 1/5 of CPU per pod
  * memory: 200 Mo per pod
* Connect to the cluster through a proxy with the following command or use port-forwarding to test your application:

```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001 
```

Now should be able to access to the **webnodb** web page at the following url `http://127.0.0.1:8001/api/v1/namespaces/__your_namespace_name__/services/__your_service_name__/proxy/`
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References
* [Kubernetes YAML File Explained - Deployment and Service](https://youtu.be/qmDzcu5uY1I?si=jeoMTcyKxxQ70jmG)
* [Accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/)
* [Manually constructing apiserver proxy URLs](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/#manually-constructing-apiserver-proxy-urls)
* [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
  
## Challenge 8: Deploy on the Kubernetes cluster your website (webdb) and the respective mongodb database (2pts)

* Deploy the webdb web service with 3 replica and its related service (**NodePort**)
* Deploy the mongodb database and its related service (**ClusterIP**)
* Connect the web service to the database using kubernetes DNS hostname
* Explain the difference between a NodePort Service and a ClusterIP service
* Validate your deployment (webdb, mongodb) by using port-forwarding
* Request the following resources per pod:
  * cpu resource: 1/10 CPU per pod 
  * memory: 100 Mo per pod
* Limit your pod resources as the following:
  * cpu resourse: 1/5 of CPU per pod
  * memory: 200 Mo per pod 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References 
* [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)

## Challenge 9: Expose your services (1pts)
* Create a Ingress in order to expose your web application (webnodb and webdb)
  * GKE has some custom-made feature in order to deploy Ingress, be sure to read carefully to Ingress documentation of [GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress?hl=fr)
  * Don't forget to deploy your ingress in your own namespace !!!
* The kubenetes cluster has a public IP address with the hostname: "net4255.luxbulb.org" create a service that redirects http traffic of the following url to your respective deployment: 
  * url 1: http://webnodb.your_name.net4255.luxbulb.org/ => deployment webnodb
  * url 2: http://webdb.your_name.net4255.luxbulb.org/ => deployment webdb
* Test your Ingress 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

**Warning, please call the teacher before applying your Ingress.**

### References
* [GKE ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress?hl=fr)

## Challenge 10: Automate your deployment with HELM (1pts)
* Create a HELM Chart to deploy the whole infrastructure 
* Use ConfigMaps to store database hostname and port information

### References
* [Use ConfigMap in Kubernetes](https://kubernetes.io/docs/concepts/configuration/configmap/)

## Challenge 11: Update the mongodb database Deployment with a StatefulSet (1pts)
* Instead of a traditional deployment use a StafulSet to deploy your mongodb database 
* Use a Persistant Volume to store the database content
    *  Stockage ressource : 0.1 Go
* Update the previous mongodb service with a headless service
* There should be only one replicat for the mongodb database
* Explain what is a StatefulSet and in which case it is usefull
* Explain what is a headless service, how pods are named with headless service
* Update your previous Helm chart accordinly 
* Your first database in the statefulSet (example: mongo-0) should have a valid DNS hostname

### References
* [Kubernetes StatefulSet simply explained](https://youtu.be/pPQKAR1pA9U?si=as0jDo02sCPmBR43)
* [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
* [Tutorial/Howto about StatefulSet](https://redhat-scholars.github.io/kubernetes-tutorial/kubernetes-tutorial/statefulset.html)
* [Kubernetes Volumes explained](https://youtu.be/0swOh5C3OVM?si=LNfXMlxe39_wbazI)
* [GKE Volumes persistants et provisionnement dynamique](https://kubernetes.io/fr/docs/concepts/storage/persistent-volumes/)
* [How to set pvc with statefulset in kubernetes?](https://stackoverflow.com/questions/65266223/how-to-set-pvc-with-statefulset-in-kubernetes)

## Challenge 12: Rolling update (1pts)
* Update the version number in each of the HTML page of the respective website (webdb and webnodb) and rebuild their repective docker container (and bump up their version humber)
* Deploy your new container as a rolling update 

### References 
* [Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

## Challenge 13: Automatic scaling (1pts)
* Create a deployment that spin a new pod when the CPU utilization of a pod cross a certain threasold (e.g.: 60% Utilization)
* Limit to maximum number of pods to be deploy to 10 pods

### References
* [Horizontal Scaling with Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

## Challenge 14: Liveness Probes (1pts)
* Define **Liveness Probe** for each container in your Chart
* Becareful each application might need a specific type of probe 
* Explain you choose a spefic type of probe for a given application

### References 
* [Configure Liveness Probes in Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

## Challenge 15: Create a Network policies (1pts)
* Create a Network policy that restrict access to the database only to IP address corresponding to your Web Pods 
* Test your network policy 

### References 
* [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

## Challenge 16: Create a distributed database system (I) (2pts)
* Create a master-slave architecture with mongodb
* Don't use already made Helm chart to achive this challenge
* Manualy configure each instance of the mongodb database to be part of a Replica Set (meaning that a given master database is replicated to all the slaves in the cluster) 

### References
* [Replication Introduction](https://www.mongodb.com/docs/v2.4/core/replication-introduction/)
* [Deploy a Replica Set](https://www.mongodb.com/docs/v2.4/tutorial/deploy-replica-set/)
* [Kubernetes StatefulSet explained](https://youtu.be/pPQKAR1pA9U?si=pjmaqy5EvE3P4W2c)
* [Statefulsets | Deploying MongoDB clusters to Kubernetes](https://youtu.be/eUa-IDPGL-Q?si=wcZc2AVhYXit0OSD)

## Challenge 17: Create a distributed database system (II) (1pts)
* Create a Helm Chart that deploy a master-slave architecture with mongodb 

## Challenge 18: Deploy a Redis cache in your infrastructure (1pts)
* Explain what is the advantage of updating your infrastructure with a redis cache ?
* Define your new infrastructure

### References 
* [Redis Cache](https://www.geeksforgeeks.org/redis-cache/)

## Challenge 19: Implement Hooks on Helm
* Use Hooks to configure your ConfigMaps before and after the deployment of your helm chart
* (Optional) Use hooks to save your database before updating helm chart

### References 
* [Helm Chart Hooks](https://www.golinuxcloud.com/kubernetes-helm-hooks-examples/)
