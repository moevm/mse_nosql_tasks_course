#!/bin/bash

apt-key add scripts/mongodb_key.asc

echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list

apt-get update

apt-get install -y mongodb-org

mkdir  -p /data/db
timeout --foreground 2 mongod --fork --logpath /var/log/mongodb.log
