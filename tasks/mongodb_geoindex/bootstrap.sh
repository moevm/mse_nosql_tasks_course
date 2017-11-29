#!/usr/bin/env bash
echo "
-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA5ika8lRKCwv+c8amk4NHIo76tkm1fu497iV6ng5U+vcT/5RS
r2Cag880qxXARlZvfLCyz31GQE0akIzLpp7UEdGTK/ZrpBzhcl4Yii+mXGYLd+Mp
qgRDZ57vg6js/k3/xpic82Gg3d25ZTPRyF4QB8YzRPvI+TgHp3qNgEgxTMCk7Zp8
db92ALftczzp9q/P8QKJatcECk1xCERMOdWKOXrWKIeGY96TLo0xEtoGp9e+LF2Y
zJJb4REVSBzNNE8QQD/kNp/9hGgxCUj+urR1l6vMSvT9mRS8IEJed0ZwVbg4pyCT
gElXBYvRy2gNSevxWpkq4ao2n4eRKqtpuauRAwIDAQABAoIBAQC904EqBGLdIZNH
obuZRljRI+ObnMdYXN4vIDI1UdS8+DNCQ+6+Poqx05+4y0O9v2RMDuArSUM7nVwf
hEAiuDRoTdV4GNFGlZtLXFgZAJvQ8UjcJDskwkdlmywoBpcQVvxxq0UnZonq8wgJ
c+e9vfayssFuT8u94HxPoUA7YU9n4JpQ8EnlhVUhtfptdi2oFcAYIWySW3NGT0S0
ghJGMHS3kV4SjYj0CpZy4YVeWO1KvrFO4gvKmTpQK+nHSpVFKEXCExAspcil2+MC
uNBXYyFg08VUUtAmysXAPBrxmiTkY/vMJ3qKqf2QK7WjLv0f8Nqed90zZmqyIxz6
kxUjGd/hAoGBAP5DcSnGT57mCpYPlj4Rx5JngcBaIVNAFX9tb3uLaspzTkaCRjC0
SS7wlm0IKgo835KSQ+sxRbV/v1N69yJp/upfLdtqsMlycmyBP45bI+G6ihykwkjg
dy36bFoZANVTN7jC9+2ufLhv4BNJuXzjAI1bWxo9X9Yxc7gazHRSFz23AoGBAOe7
hXnCet9ZhV4KoH/pqkV3TxcPzN8GkHoj9YAlZVYLJFTTkqXVYWU9OaiNt5p+gGHy
Z5qj0diO3vFbOxdJtYHh8CGw/FhLTZw5PyH6phODdfYCa5g9WOWjo5vq/PWqzX1y
XHyV7nQjY+qKEkmhLx/zaL/AVJ2oHZb0tDOliIcVAoGBAJDXMF6gtniJCNzE0kxX
an2O8w31CejXp6doWspg+BuNpbhqu7tA6DOSH87KiNA+Lwnawk/3SIOE2yOd96wl
/23ZfFDyrPSEeoQu+FqKtpz+23BHttk27Q1HC3QjrCLZffOFNSCzdh7GtDmolL58
vbLIqNQAxFhK4WWt9mwI225vAoGBAMHxvfpz/GZmBCr69e1YYTuWaUlB3hNi6RRw
eA3yPmfPF28vS/MjLUqP/WvGgD37VfOj73YLWZvHp2uVEVWiSRkVQebQu8Ih9Cil
+OK1Zr26LsXgrLBT180KMepSt7fcZfNx/VoAGfx1ijBHspqRHmG9VJP3oln41Br9
XrxC9IspAoGBAJa+X1JuDXSxuJAI4jJ5MYDWQNhY7F/6aSccPSPemqblczNsSC/8
46idw5yOd6h9JBWI8LvsNeqgoqYYF//BReGEB7syyPmcHIsgBJQbyFgdoV2QFWqr
oc9DcG1pKaPRDYNP7wUWg6LI4VSaslJKB5TvOnFJ+58xtRBvDuEFGX2E
-----END RSA PRIVATE KEY-----
" > .ssh/id_rsa

echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDmKRryVEoLC/5zxqaTg0cijvq2SbV+7j3uJXqeDlT69xP/lFKvYJqDzzSrFcBGVm98sLLPfUZATRqQjMumntQR0ZMr9mukHOFyXhiKL6ZcZgt34ymqBENnnu+DqOz+Tf/GmJzzYaDd3bllM9HIXhAHxjNE+8j5OAeneo2ASDFMwKTtmnx1v3YAt+1zPOn2r8/xAolq1wQKTXEIREw51Yo5etYoh4Zj3pMujTES2gan174sXZjMklvhERVIHM00TxBAP+Q2n/2EaDEJSP66tHWXq8xK9P2ZFLwgQl53RnBVuDinIJOASVcFi9HLaA1J6/FamSrhqjafh5Eqq2m5q5ED vood@vood-ThinkPad"
> .ssh/id_rsa.pub

chmod 600 .ssh/id_rsa
chmod 644 .ssh/id_rsa.pub

ssh-keyscan github.com >> .ssh/known_hosts

cd /home/box/
git clone git@github.com:moevm/mse_nosql_tasks_course.git repo
cd ./repo
git checkout geoindex
# /Machine setting up

# Insert your task setup here

# Here will be task initialization

 ./scripts/init_task.sh "mongodb_geoindex" "esawwr3Xv41aSZCcVgz5AxcsBBBvtREssZEbFfbz3SCqzXBDSg"
# /Insert your task setup here

# Keys and repo cleanup
rm -rf /root/.ssh/id_rsa*
rm -rf /home/box/repo
# /Keys and repo cleanup