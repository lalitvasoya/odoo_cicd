#!/bin/bash

echo "****************************"
echo "**   Building the docker  **"
echo "****************************"


# change dir to worksapce
cd flask_demo

source env.sh

git checkout $BRANCH
git pull https://$USERNAME:$PASSWORD@github.com/lalitvasoya/odoo_cicd.git $BRANCH 

echo $BRANCH
echo $USERNAME
echo $PASSWORD

# up the build
docker-compose up --build -d