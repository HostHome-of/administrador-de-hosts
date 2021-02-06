#!/bin/bash

cd logs/
directorio=`pwd`
archivo=$directorio"\\"$2.out
cd ..
cd $3

cd hosthome_env
source .\\Scripts\\activate
cd ..

# echo "nohup "$1" > "$2".out & "
/usr/bin/nohup $1 > "${archivo}" & 