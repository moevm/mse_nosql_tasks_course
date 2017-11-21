#!/bin/bash

key="esawwr3Xv41aSZCcVgz5AxcsBBBvtREssZEbFfbz3SCqzXBDSg"

cd /home/box/repo/tasks/mongodb_geowithin-task2/
python3 gw_task2_creation.py
mv correct_answer /home/box/
cd /home/box/
rm -rf repo

echo ${key} | gpg --no-tty --passphrase-fd 0 -c /home/box/correct_answer
chown box:box /home/box/correct_answer.gpg
sudo rm -f /home/box/correct_answer