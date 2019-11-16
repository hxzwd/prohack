#!/home/hjk/croc_hack/bin/ipython3 --no-banner
#-*- coding: utf-8 -*-

import os
import sys
import json


from flask import Flask, request


from misc import c_linreg_model


from api import api


from IPython import embed


global flask_app
global server_config


flask_import_name = __name__
server_config = None


flask_app = Flask(flask_import_name)



def f_print_hello():
	print("[main.py]: hello from main.py")


def f_get_config(config_file = "main.conf", section = ""):
	print("[f_get_config]: read config data from file {} for section \"{}\"".format(config_file, "none" if section == "" else section))
	f = open(config_file, "r")
	data = f.read()
	f.close()
	config_data = json.loads(data)
	if section == "":
		return config_data
	else:
		if section in config_data.keys():
			return config_data[section]
		else:
			return config_data


def is_none(obj):
	return isinstance(obj, type(None))


def f_run_app(app, server_config = { }):
	app.run(**server_config)


def f_reg_api(api):
	global flask_app
	flask_app.register_blueprint(api)


@flask_app.route("/post", methods = [ "POST" ])
def h_post_route():
	print("[h_post_route]: enter in h_post_route")
	json_data = None

	if request.method == "POST":
		json_data = request.get_json(force = True)

	if not is_none(json_data):
		print("[h_post_route]: json_data =\n{}".format(json_data))

	embed()


@flask_app.route("/api/v1.0/linreg", methods = [ "POST" ])
def h_linreg_route():
	print("[h_linreg_route]: enter in h_linreg_route")

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)
	
	#embed()

	if not is_none(json_data):
		print("[h_linreg_route]: json_data =\n{}".format(json_data))
		output_json_data = c_linreg_model.do(input_json_data = json_data)
	else:
		print("[h_linreg_route]: input json data is empty")
		output_json_data = { }

	print("[h_linreg_route]: output_json_data =\n{}".format(output_json_data))

	return str(output_json_data)







def main():
	global flask_app
	global server_config
	#flask_import_name = __name__
	f_print_hello()
	#flask_app = Flask(flask_import_name)
	print("[main]: run flask application")
	server_config = f_get_config(section = "server")
	f_reg_api(api)
	f_run_app(flask_app, server_config = server_config)


if __name__ == "__main__":
	main()


