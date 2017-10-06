#!/bin/bash


# Usage

# ./tasks/<task_name>/init_task.sh encryption_key

./scripts/install_mongodb.sh
./scripts/setup_one_time_autorun_scripts.sh ./tasks/mongodb_intro/generate_conditions.sh $1
