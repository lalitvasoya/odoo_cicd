#!/bin/bash

echo "****************************"
echo "**   Building the docker  **"
echo "****************************"


echo "Branch name: $1"
echo "USERNAME: $2"
echo "PASSWORD: $3"


git checkout $1
git pull https://$2:$3@github.com/lalitvasoya/odoo_cicd.git $1


# up the build
docker-compose up --build -d
