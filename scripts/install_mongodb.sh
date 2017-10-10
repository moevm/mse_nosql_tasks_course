#!/bin/bash

timeout --foreground 2 mongod --fork --logpath /var/log/mongodb.log
