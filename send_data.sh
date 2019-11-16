#!/bin/bash

HOST="127.0.0.1"
PORT=5000
TARGET="post"
DATA_FILE=json_data.json
DATA=""

PORT=8000
DATA_FILE=data_for_linreg.json
TARGET="linreg"
TARGET="api/v1.0/linreg"
TARGET="api/v1.0/metal_temperature"
TARGET="api/v1.0/metal_concentration/valc"
TARGET="api/v1.0/metal_concentration/valsi"
TARGET="api/v1.0/metal_concentration/valcu"


echo "read json data from: $DATA_FILE"
echo
DATA=$(cat $DATA_FILE)

echo "send json data to $HOST:$PORT/$TARGET"
echo
curl "$HOST":"$PORT""/""$TARGET" -d "$DATA" -H "Content-Type: application/json"

