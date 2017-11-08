#!/bin/bash

# Usage
# ./scripts/init_task.sh memcached_get_key_names encr_key

TASK=$1
KEY=$2
DB=`echo "${TASK}" | grep -o "^[^_]\+"`

./scripts/install_${DB}.sh
./scripts/setup_one_time_autorun_scripts.sh ./tasks/${TASK}/generate_conditions.sh ${KEY}
