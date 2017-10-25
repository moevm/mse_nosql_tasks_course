#!/bin/bash

key="esawwr3Xv41aSZCcVgz5AxcsBBBvtREssZEbFfbz3SCqzXBDSg"



cd /home/box/repo/tasks/mongodb_geointersects/
python3 geointersects_creation.py
mv correct_answer /home/box/

cd /home/box/
echo ${key} | gpg --no-tty --passphrase-fd 0 -c /home/box/correct_answer
chown box:box /home/box/correct_answer.gpg
rm /home/box/correct_answer