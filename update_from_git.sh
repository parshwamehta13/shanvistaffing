#! /bin/sh

git fetch --all
git reset --hard origin/master
./apache2/bin/restart