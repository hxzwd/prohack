#!/home/hjk/croc_hack/bin/ipython3 --no-banner
#-*- coding: utf-8 -*-

import os
import sys


from flask import Flask, request


from IPython import embed

global flask_app
flask_import_name = __name__
flask_app = Flask(flask_import_name)

def f_print_hello():
	print("[main.py]: hello from main.py")


def is_none(obj):
	return isinstance(obj, type(None))


def f_run_app(app):
	app.run()



@flask_app.route("/post", methods = [ "POST" ])
def h_post_route():
	print("[h_post_route]: enter in h_post_route")
	json_data = None

	if request.method == "POST":
		json_data = request.get_json(force = True)

	if not is_none(json_data):
		print("[h_post_route]: json_data =\n{}".format(json_data))

	embed()


def main():
	global flask_app
	#flask_import_name = __name__
	f_print_hello()
	#flask_app = Flask(flask_import_name)
	print("[main]: run flask application")
	f_run_app(flask_app)


if __name__ == "__main__":
	main()


