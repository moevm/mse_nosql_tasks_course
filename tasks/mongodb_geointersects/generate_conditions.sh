#!/bin/bash

key="esawwr3Xv41aSZCcVgz5AxcsBBBvtREssZEbFfbz3SCqzXBDSg"

python3 /home/box/repo/geointersects_creation.py

cd /home/box/
echo ${key} | gpg --no-tty --passphrase-fd 0 -c /home/box/correct_answer
chown box:box /home/box/correct_answer.gpg
rm /home/box/correct_answer