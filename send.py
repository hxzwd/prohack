#!/usr/local/bin/ipython3 --no-banner
#-*- coding: utf-8 -*-

import os
import sys
import json
import requests

host = "68.183.213.199"
port = 8080
target = "api/v1.0/metal_temperature"

data = {
	"foo" : "bar"
}

json_encoder = json.JSONEncoder()
data_encoded = json_encoder.encode(data)

url = "http://{}:{}/{}".format(host, port, target)

result = requests.post(url, data = data_encoded)
answer = result.content

print("answer =\n{}".format(answer))




