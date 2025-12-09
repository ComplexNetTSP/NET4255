
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
</p>

<h1 align="center">NET 4255: High Availability Web Services</h1>

### Teacher: [Vincent Gauthier](mailto:vincent.gauthier@telecom-sudparis.eu), [Lucas Brehon-Grataloup](lucas.brehon-grataloup@telecom-sudparis.eu)
### Assistant: [Timothée Mathubert](mailto:timothee.mathubert@telecom-sudparis.eu) 

## Introduction
* Clone this repository
* Each challenge **must be validated** with a professor and then committed and pushed to your own github repository.
* Before starting a given step, present the sketch of your infrastructure to a professor.
* We strongly recommend that you use [Alpine OS](https://www.alpinelinux.org/) as the base operating system for your [docker image](https://www.docker.com/blog/how-to-use-the-alpine-docker-official-image/). 

## Challenge 0: Install
On your own computer install the following software:
* [Docker Desktop](https://docs.docker.com/get-docker/)
* [Conda](https://www.anaconda.com/download) installation steps:
    * Run the following commands (Linux systems only, WSL works too):
    ```bash
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm ~/miniconda3/miniconda.sh
    source ~/miniconda3/bin/activate
    conda init --all
    ```
    * Create & enter your virtual python environment:
    ```bash
    conda create -n [env-name]
    conda activate [env-name]
    ```
    * Install pip in your env:
    ```bash
    conda install pip
    ```
    * Install packages inside your python virtual environnement using pip:
    ```bash
    pip install [package1] [package2] ...
    ```
* IDE ([VSCode](https://code.visualstudio.com/), etc)

## Challenge 1: Create a Simple Web page and develop a docker file for your website (1 pt)

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

Now you can run the web server you just created

```bash
flask --app hello run
* Serving Flask app 'hello'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

See the [quickstart guide](https://flask.palletsprojects.com/en/3.0.x/quickstart/) for more information

### References 
* [Getting started with Flask](https://fflask.palletsprojects.com/en/3.0.x/quickstart/)
* [Containerize an application](https://docs.docker.com/get-started/02_our_app/)
* [Christian Lempa - Learning Docker // Build Container Images](https://youtu.be/JDw3ZdQcv2g?si=ZkA7qXYBYNrPpvlW)

## Challenge 2: Create docker compose to deploy a mongodb database server (1 pt)
* Find a already made [mongodb](https://www.mongodb.com/) docker container (for instance the [official mongodb docker image](https://hub.docker.com/_/mongo/tags?page=88))
* Use docker compose to deploy your mongodb database
* Test your application and add record in your database manually with the mongod command ([see the install requirement for mongodb](https://www.mongodb.com/docs/v3.0/tutorial/install-mongodb-on-windows/)
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the containers IP address or hostname
  * Show the container ports

### References
* [Docker compose getting started](https://docs.docker.com/compose/gettingstarted/)

### Why mongodb ?
MongoDB is classified as a NoSQL database program, MongoDB uses JSON-like documents. MongoDB provides high availability with replica sets. A replica set consists of two or more copies of the data. Each replica-set member may act in the role of primary or secondary replica at any time. All writes and reads are done on the primary replica by default. Secondary replicas maintain a copy of the data of the primary using built-in replication. When a primary replica fails, the replica set automatically conducts an election process to determine which secondary should become the primary. Secondaries can optionally serve read operations, but that data is only eventually consistent by default. It's easier to create a master/slave database cluster when using nosql. 

## Challenge 3: Create docker compose file to deploy a simple web service (flask + mongodb) (1 pt) 
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
* [Docker compose getting started](https://docs.docker.com/compose/gettingstarted/)
* [Configure the default network](https://docs.docker.com/compose/networking/)
* [How to get the last N records in mongodb?](https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb)

## Challenge 4: Install a load balancer for your infrastructure (1pt)

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
* [NGINX](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)

## Challenge 5: Learn Kubernetes with the online tutorial (1 pt)
* Ask the professor to get access to the Kubernetes cluster.
* Install [kubectl](https://kubernetes.io/fr/docs/tasks/tools/install-kubectl/)
* Use the provided credentials to connect in the [Rancher Web interface](https://net4255.luxbulb.org). You have access to the cluster dashboard at the same address.
* Install the kubeconfig file on your computer:
  * In Rancher web interface: go to "Cluster Management".
  * Click on the "net4255" cluster, then on "Download KubeConfig".
  * After this step you should have `net4255.yml` file on your laptop, inside your Downloads folder. This file will enable you to get access to the kubernetes cluster.
  * Move the `net4255.yml` file to `~/.kube/config`:
  ```bash
  mkdir ~/.kube
  mv ~/Downloads/net4255.yaml ~/.kube/config
  ```
  * Export the kubeconfig file
  ```bash
  export KUBECONFIG=$HOME/.kube/kubeconfig.yml
  ```
* Now, you should be able to connect to the Kubernetes cluster. Check the following command in order to check the connection.
```bash
kubectl cluster-info
...
```
* Now that you are set up, follow the [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)

### References
* [Kubernetes Tutorial](https://kubernetes.io/docs/tutorials/)
  
## Challenge 6: Launch your first Pod in command line (1 pt)
Create your first deployment in command line with the `kubectl` command: 
* Create a deployment for the "webnodb" container in your own namespace
   * Without any replicat
   * Without **any service**
* Check that your deployment is successful in the [Rancher interface](https://net4255.luxbulb.org) and with the command line: 
```bash
kubectl get deployments -o wide
...
kubectl get pods -o wide
...
```

* Test if the "webnodb" Pod is correctly running with port-forwarding using the Pod's ID:
```bash
kubectl port-forward pods/[your pod ID]:[pod port] --namespace=[your namespace]
Forwarding from 127.0.0.1:54127 -> 5000
```
In this example, you can connect with your browser to `http://127.0.0.1:54127` to access the "webnodb" website.


### References
* [Deploying your first app on Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
* [Using Port Forwarding to access a pod inside a Kubernetes cluster](https://kubernetes.io/fr/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)

## Challenge 7: Create your first deployment file with a ClusterIP service (1 pt)
* Create a Deployment file for your container "webnodb" (**the one without database**)
* Be careful, create your **Deployment** and **the ClusterIP service** in your on namespace !!!!
* Show on a new schema how a request is served from the service to the pods:
  * The schema should explain which port is used at each step and what IP address is used by each component (nodes, pods, services)
* Request the following resources per pod:
  * CPU resource: 1/10 CPU per pod 
  * Memory (RAM): 100 Mo per pod
* Limit your pod resources as the following:
  * CPU resource: 1/5 of CPU per pod
  * Memory (RAM): 200 Mo per pod
* Connect to the cluster through a Proxy with the following command (you can still use port-forwarding to check if the pod is running, for debug purposes):

```bash
kubectl proxy
Starting to serve on 127.0.0.1:8001
```
Now should be able to access to the **webnodb** web page at the following url `http://127.0.0.1:8001/api/v1/namespaces/[namespace_name]/services/[service_name]/proxy/`
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References
* [Kubernetes YAML File Explained - Deployment and Service](https://youtu.be/qmDzcu5uY1I?si=jeoMTcyKxxQ70jmG)
* [Accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/)
* [Manually constructing apiserver proxy URLs](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/#manually-constructing-apiserver-proxy-urls)
* [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
  
## Challenge 8: Deploy on the Kubernetes cluster your website (webdb) and the respective mongodb database (1 pt)

* Deploy the "webdb" web service with 3 replica and its related service (**ClusterIP**)
* Deploy the "mongodb" database and its related service (**ClusterIP**)
* Connect the "webdb" Pod to the database using KubeDNS
* Explain the difference between a NodePort Service and a ClusterIP service
* Validate your deployment ("webdb", "mongodb") by using port-forwarding & KubeProxy
* Request the following resources per pod:
  * CPU resource: 1/10 CPU per pod 
  * Memory (RAM): 100 Mo per pod
* Limit your pod resources as the following:
  * CPU resourse: 1/5 of CPU per pod
  * Memory (RAM): 200 Mo per pod 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports 

### References
* [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/)

## Challenge 9: Liveness Probes (1 pt)
* Define a **Liveness Probe** for each container.
* Note that each application may require a specific type of probe.
* Explain why you have chosen a particular type of probe for a particular application.
    * What is your liveness probing strategy for the web servers?
    * What is your liveness probing strategy for the database?

### References 
* [Configure Liveness Probes in Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

## Challenge 10: Expose your services (1 pt)
* Create a Ingress in order to expose your web application ("webnodb" and "webdb")
  * In the cluster, we use MetalLB (bare metal load balancer) to handle incoming Ingress traffic. [Here](https://8grams.medium.com/metallb-a-load-balancer-for-bare-metal-kubernetes-clusters-ef8a9e00c2bd) you can find some documentation about the specifics of MetalLB (only useful for the schema).
  * Don't forget to deploy your Ingress in your own namespace !!!
* The kubenetes cluster has a public IP address with the hostname: `net4255.luxbulb.org` create a service that redirects http traffic of the following url to your respective deployment: 
  * url 1: http://webnodb.[your_namespace].net4255.luxbulb.org/ => deployment webnodb
  * url 2: http://webdb.[your_namespace].net4255.luxbulb.org/ => deployment webdb
* Test your Ingress 
* Update the schema of your infrastructure (ex. [draw.io](https://app.diagrams.net))
  * Show the system
  * Show the container IP address and the hostname of each container
  * Show the container ports

### References
* [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

## Challenge 11: Automate your deployment with HELM (1 pt)
* Create a HELM Chart to deploy the whole infrastructure
* Use ConfigMaps to store database hostname and port information

### References
* [Use ConfigMaps in Kubernetes](https://kubernetes.io/docs/concepts/configuration/configmap/)
* [Getting started with HELM](https://helm.sh/docs/chart_template_guide/getting_started/)

## Challenge 12: Update the mongodb database Deployment with a StatefulSet (1 pt)
* Instead of a traditional deployment use a StafulSet to deploy your "mongodb" database 
* Use a Persistant Volume to store the database content
  *  Stockage ressource : 0.1 Go
* Update the previous "mongodb" service with a **headless service**
* **There should be only one replicat for the "mongodb" database**
* What is a StatefulSet and in which case it is usefull?
* What is a headless service, how pods are named with headless service?
* Update your previous Helm chart accordinly
* Your first database in the StatefulSet (example: mongo-0) should have a valid DNS hostname
* As storageClassName in your Persistent Volume Claim, set `longhorn`

### References
* [Kubernetes StatefulSet simply explained](https://youtu.be/pPQKAR1pA9U?si=as0jDo02sCPmBR43)
* [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
* [Tutorial/Howto about StatefulSet](https://redhat-scholars.github.io/kubernetes-tutorial/kubernetes-tutorial/statefulset.html)
* [Kubernetes Volumes explained](https://youtu.be/0swOh5C3OVM?si=LNfXMlxe39_wbazI)
* [Kubernetes persistent volumes and dynamic provisionning](https://kubernetes.io/fr/docs/concepts/storage/persistent-volumes/)
* [How to set a Persistent Volume Claim with StatefulSet in Kubernetes?](https://stackoverflow.com/questions/65266223/how-to-set-pvc-with-statefulset-in-kubernetes)

## Challenge 13: Rolling update (1 pt)
* Update the version number in each of the HTML page of the respective website ("webdb" and "webnodb") and rebuild their repective docker container (and bump up their version humber)
* Deploy your new container as a rolling update

### References 
* [Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

## Challenge 14: Automatic scaling (1 pt)
* Create a deployment that spin a new pod when the CPU utilization of a pod cross a certain threasold (e.g.: 60% Utilization)
* Limit to maximum number of pods to be deploy to 10 pods

### References
* [Horizontal Scaling with Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

## Challenge 15: Create a Network policies (1 pt)
* Create a Network policy that restrict access to the database only to IP address corresponding to your Web Pods
* Test your network policy 

### References 
* [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

## Challenge 16: Create a distributed database system (I) (1 pt)
* Create a master-slave architecture with mongodb
* Don't use already made Helm chart to achive this challenge
* Manualy configure each instance of the mongodb database to be part of a Replica Set (meaning that a given master database is replicated to all the slaves in the cluster)

### References
* [Replication Introduction](https://www.mongodb.com/docs/v2.4/core/replication-introduction/)
* [Deploy a Replica Set](https://www.mongodb.com/docs/v2.4/tutorial/deploy-replica-set/)
* [Kubernetes StatefulSet explained](https://youtu.be/pPQKAR1pA9U?si=pjmaqy5EvE3P4W2c)
* [Statefulsets | Deploying MongoDB clusters to Kubernetes](https://youtu.be/eUa-IDPGL-Q?si=wcZc2AVhYXit0OSD)

## Challenge 17: Create a distributed database system (II) (1 pt)
* Create a Helm Chart that deploy a Master-Slave architecture with mongodb 

## Challenge 18: Create a REST API endpoint instead of directly querying the database (1 pt)
* Develop a new flask container which will handle the REST API GET request:
  * Your endpoint should be in the form "http://webdb.[your_namespace].net4255.luxbulb.org/api/db?limit=10", which should return the 10 most recent elements inserted into the database.
  * The REST API endpoint should be exposed to the Ingress controler at the following url: http://webdb.[your_namespace].net4255.luxbulb.org/api/

### References
* [Building a rest API with flask](https://www.geeksforgeeks.org/python/python-build-a-rest-api-using-flask/)
  
## Challenge 19: Update your web server to use the REST API instead of the of database query (1 pt)
* Modify your website so that the REST API request is made directly from a JavaScript function in your HTML, rather than from the Flask backend.

```html
<HTML>
<HEAD>
  <TITLE>Sample HTML Page</TITLE>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
    $(window).on('load', async function() {
      // Replace the below JSON data with your get request to fetch data
      var jsonData = await loadData();
      //
      console.log(jsonData);
      var datatable = document.getElementById('data');
      var ul = document.createElement('ul');
      for (var i = 0; i < jsonData.length; ++i) {
        var li = document.createElement('li');
        li.innerHTML = jsonData[i].title;
        ul.appendChild(li);      
      }
      datatable.appendChild(ul);                               
    });   

    async function loadData() {
      const resp = await fetch("https://dummy-json.mock.beeceptor.com/todos");
      const data = await resp.json();
      return data;
    }
  </script>
</HEAD>
<BODY>
    <H1>Welcome to the Sample HTML Page</H1>
    <P>This is a simple HTML document used to demonstrate basic HTML structure.</P>
    <div id="data"></div>
</BODY>
</HTML>
```

## Challenge 20: Deploy a Redis cache in your infrastructure (1 pt)
* Your webpage should display the number of visitor who requested the webpage nad remain consistent across replicas.
  * Create a new endpoint in your REST API http://xxxxx/api/v1/visit which implement a GET request
  * Create a new endpoint in your REST API http://xxxxx/api/v1/visit which implement a POST request
  * Each time a page is loaded, your page should send a post request to API endpoint which will in turn increment the number of visit in a REDIS cache.
  *  
* Explain the advantage of using a redis cache in this case.
* Update the drawing of your new infrastructure (services, etc)

### References 
* [Redis Cache](https://www.geeksforgeeks.org/redis-cache/)
