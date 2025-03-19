# Hands on commands

## To install pip3 and install flask

```jsx
sudo apt-get update && sudo apt install python3-pip
pip3 install flask
```

## Command to start a docker container

```jsx
 sudo docker run -p 5000:5000 -d --name webapp webapp
```

## Docker to containerd image import

```jsx
 sudo docker save -o my-webapp.tar webapp:latest
 sudo ctr -n k8s.io images import my-webapp.tar
```

## Kubernetes command to apply the deployment

```jsx
sudo kubectl apply -f deployment.yaml
```