#!/bin/bash

DIR=$(dirname $0)

source $DIR/src/config.sh

docker run -it --rm iman/syn-attacker:1 bash dispatch.sh
