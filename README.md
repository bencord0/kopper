Kopper
======

Kubernetes Code Deployer

Architecture
============

1. During CI runs, a Docker Image is pushed to a registry
2. Registry sends a [webhook][RegistryNotifications] to Kopper
3. Kopper prepares a release, creates a Deployment object
4. Kubernetes updates Pods to use the new Deployment.

[RegistryNotifications]: https://docker.github.io/registry/notifications/
You can setup a hook with the a stanza like this in the registry config.yml

```
...
notifications:
 endpoints:
  - name: kopper
    url: "http://172.17.0.1:8000/event/"
```

Running the server locally
==========================

    export SECRET_KEY=$(uuidgen)
    export ALLOWED_HOSTS="*"
    export DEBUG=1  # optional

    pipenv install
    pipenv run ./manage.py runserver

Running the example
===================

Create the base kubernetes resources

    kubectl apply -f examples

Push a replacement docker image

    make -C examples/app

Wait for kubernetes to deploy the new Pods.

Done!
