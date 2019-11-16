
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
		

