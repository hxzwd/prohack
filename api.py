

import os
import sys


import numpy as np
import pandas as pd


from flask import Flask
from flask import request
from flask import Blueprint






global template_folder
template_folder = "templates"


global api
api = Blueprint("api", __name__, template_folder = template_folder)


def is_none(obj):
	return isinstance(obj, type(None))







@api.route("/api/v1.0/metal_temperature", methods = [ "POST" ])
def h_metal_temperature_route():
	func_key = "metal_temperature"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_oxidity", methods = [ "POST" ])
def h_metal_oxidity_route():
	func_key = "metal_oxidity"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration", methods = [ "POST" ])
def h_metal_concentration_route():
	func_key = "metal_concentration"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/valc", methods = [ "POST" ])
def h_metal_concentration_valc_route():
	func_key = "metal_concentration_valc"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)



@api.route("/api/v1.0/metal_concentration/valsi", methods = [ "POST" ])
def h_metal_concentration_valsi_route():
	func_key = "metal_concentration_valsi"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/valmn", methods = [ "POST" ])
def h_metal_concentration_valmn_route():
	func_key = "metal_concentration_valmn"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/valp", methods = [ "POST" ])
def h_metal_concentration_valp_route():
	func_key = "metal_concentration_valp"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/vals", methods = [ "POST" ])
def h_metal_concentration_vals_route():
	func_key = "metal_concentration_vals"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/valcu", methods = [ "POST" ])
def h_metal_concentration_valcu_route():
	func_key = "metal_concentration_valcu"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)


@api.route("/api/v1.0/metal_concentration/valcr", methods = [ "POST" ])
def h_metal_concentration_valcr_route():
	func_key = "metal_concentration_valcr"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)



@api.route("/api/v1.0/metal_concentration/valmo", methods = [ "POST" ])
def h_metal_concentration_valmo_route():
	func_key = "metal_concentration_valmo"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)



@api.route("/api/v1.0/metal_concentration/valni", methods = [ "POST" ])
def h_metal_concentration_valni_route():
	func_key = "metal_concentration_valni"
	print("[h_{0}_route]: enter in h_{0}_route".format(func_key))

	json_data = None
	output_json_data = None


	if request.method == "POST":
		json_data = request.get_json(force = True)


	if not is_none(json_data):
		print("[h_{}_route]: json_data =\n{}".format(func_key, json_data))
		output_json_data = { }
	else:
		print("[h_{}_route]: input json data is empty".format(func_key))
		output_json_data = { }

	print("[h_{}_route]: output_json_data =\n{}".format(func_key, output_json_data))

	return str(output_json_data)