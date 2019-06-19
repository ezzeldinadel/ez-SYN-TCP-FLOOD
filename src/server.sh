#!/bin/bash

mkdir -p out

cd out

port="$1"

if [[ -z ${1+x} ]]
then
    port=8001
fi

python -m http.server $port

