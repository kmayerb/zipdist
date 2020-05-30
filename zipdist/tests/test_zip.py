from zipdist.zip import Zipdist
import pytest
import pandas as pd
import numpy as np
import sys
import os

# suppose Y is your python Class
def test_basic_example():
	class Y(Zipdist):
		def __init__(self, name):
			self.name = name
			self.year = None

	y = Y('Simpsons')
	y.years = [2020,2019]
	y.bart = np.zeros(10)
	y.lisa = pd.DataFrame([{"Pi":3.1415,"e":2.7182}])
	y._save()
	assert os.path.isfile("Simpsons.tar.gz")

	 # Create a New Object, None of the prior attributes exists
	assert os.path.isfile("Simpsons.tar.gz")
	y2 = Y("Simpsons")
	assert 'bart' not in y2.__dict__.keys()
	assert 'years' not in y2.__dict__.keys()
	# But you can rebuilt it
	y2._build(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
	assert isinstance(y2.bart, np.ndarray)
	assert isinstance(y2.lisa, pd.DataFrame)

	assert 0

