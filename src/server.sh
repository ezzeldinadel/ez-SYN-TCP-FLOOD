#!/bin/bash

mkdir -p out

cd out

port=8001

if [[ -z ${1+x} ]]
then
    port="$1"
fi

python -m SimpleHTTPServer $port

