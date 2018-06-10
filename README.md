Kopper
======

Kubernetes Code Deployer

Architecture
============

1. During CI runs, a Docker Image is pushed to a registry
2. Registry sends a [webhook][RegistryNotifications] to Kopper
3. Kopper prepares a release, creates a Deployment object
4. Kopper updates Services to use the new Deployment.

Users can use terraform to setup registry hooks to kopper.
The Deployment maybe minimally scaled, scaled the same as a previous Deployment
or even autoscaled during the release.
Releases can be rolled back via API or web UI.

[RegistryNotifications]: https://docker.github.io/registry/notifications/

Running the server locally
==========================

    export SECRET_KEY=$(uuidgen)
    export ALLOWED_HOSTS="*"
    export DEBUG=1  # optional

    pipenv install
    pipenv run ./manage.py runserver

Running in docker
=================

    docker build -t registry.condi.me/kopper .

    docker run \
      -e SECRET_KEY=$(uuidgen) \
      -e ALLOWED_HOSTS=localhost \
      -p 80:80
      registry.condi.me/kopper \
      piipenv run ./manage.py runserver 0.0.0.0:80
