#!/bin/bash

HOST="127.0.0.1"
PORT=5000
TARGET="post"
DATA_FILE=json_data.json
DATA=""


echo "read json data from: $DATA_FILE"
echo
DATA=$(cat $DATA_FILE)

echo "send json data to $HOST:$PORT/$TARGET:"
echo
curl $HOST:$PORT/$TARGET -d "$DATA"

