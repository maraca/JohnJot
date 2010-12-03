#!/bin/bash

file='../manage.py'
if ! [ -x $file ]; then
  chmod u+x $file
fi

$file dumpdata auth.user auth.group core --indent 2 >> initial_data.json
