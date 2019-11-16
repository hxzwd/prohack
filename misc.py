
import os
import sys

import numpy as np
import pandas as pd

from sklearn import linear_model


class c_linreg_model:


	model = None

	def __init__(self):
		self.model = None
		self.model = linear_model.LinearRegression()


	def fit(self, X_train = [], Y_train = []):
		self.model.fit(X_train, Y_train)		
		pass


	def predict(self, X_pred = []):
		Y_pred = []
		Y_pred = self.model.predict(X_pred)
		return Y_pred


	@staticmethod
	def do(input_json_data = { }):
		output_json_data = { }
		result = { }
		X_train = input_json_data["data"]["X"]
		Y_train = input_json_data["data"]["Y"]
		X_pred = input_json_data["predict"]["X"]
		#X_train = map(list, X_train)
		#Y_train = map(list, Y_train)
		#X_pred = map(list, X_pred)
		X_train = [ [ x ] for x in X_train ]
		X_pred = [ [ x ] for x in X_pred ]
		linreg_model = c_linreg_model()
		#embed()
		linreg_model.fit(X_train = X_train, Y_train = Y_train)
		Y_pred = linreg_model.predict(X_pred = X_pred)
		result["Y_pred"] = Y_pred
		output_json_data["result"] = result
		return output_json_data


