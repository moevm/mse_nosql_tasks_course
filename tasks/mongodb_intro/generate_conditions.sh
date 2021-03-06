#!/bin/bash

key="KEY"

db_name=`< /dev/urandom tr -dc A-Za-z0-9 | head -c6`
mongo ${db_name} --eval 'db.test.insert({"name":"foo"});' --quiet
echo "${db_name}" > /home/box/correct_answer

cd /home/box/
echo ${key} | gpg --no-tty --passphrase-fd 0 -c /home/box/correct_answer
chown box:box /home/box/correct_answer.gpg
rm /home/box/correct_answer
