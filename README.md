# My first full-fledged DevOps project

Among the technologies used are: Kubernetes, Ansible, Docker, Nginx, Flask, MySQL, Jenkins, Prometheus and Grafana

___

## Ansible

Thanks to Ansible and its playbook, IaC can be organized.
Playbooks from this repository allow you to install Docker Engine, Kubernetes based on cri-dockerd (including the Go language for building this plugin)

## Python Flask & MySQL

A small web application written in Flask is used as an example of an infrastructure application, and MySQL is also used as a database.

Thanks to Dockerfile's applications are assembled into images and go to registry

## Kubernetes

The beloved Kubernetes is used as a container orchestration system. With its help, applications are assembled, as well as Nginx as a load balancer

## Jenkins

With the help of Jenkins, a small CI pipeline is created for assembling and sending the image to registry

## Prometheus & Grafana

Where to go without monitoring. With the help of Docker Compose, the Prometheus monitoring system is raised on one node, as well as the Grafana visualization system
Using Kubernetes, node-exporter is deployed on all nodes to build metrics

