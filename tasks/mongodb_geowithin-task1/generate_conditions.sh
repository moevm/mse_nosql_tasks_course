#!/bin/bash

key="esawwr3Xv41aSZCcVgz5AxcsBBBvtREssZEbFfbz3SCqzXBDSg"

cd /home/box/repo/tasks/mongodb_geowithin-task1/
python3 geowithin_creation.py
python3 geowithin_solution.py
rm -f geowithin_solution.py
mv correct_answer /home/box/

cd /home/box/

echo ${key} | gpg --no-tty --passphrase-fd 0 -c /home/box/correct_answer
chown box:box /home/box/correct_answer.gpg
sudo rm -f /home/box/correct_answer