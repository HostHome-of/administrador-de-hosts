#!/bin/bash

cd logs/
directorio=`pwd`
archivo=$directorio"\\"$2.out
cd ..
cd projectos
cd $2

# echo "nohup "$1" > "$2".out & "
nohup $1 > "${archivo}" & 