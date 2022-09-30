# Abraxas DevOps Exercise

## Download Repo to your local
* git clone https://github.com/mamanzano/devops-exercise.git
* Create a virtual environment in my case use conda
* Install dependencies found in the requirement.txt file
* Execute flask app

## Application servicies:
* Method: Get
    * http://127.0.0.1:5000

        return a string

* Method Post
    * http://127.0.0.1:5000

## Create your deploy and service into kubernetes

You'll need:

1. copy the files found in the folder **manifest** to your master node
2. Execute the next commands
    * kubectl apply -f ./deployment-apptest.yaml
    * kubectl apply -f ./service-apptest.yaml