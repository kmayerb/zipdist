from zipdist.zip2 import Zipdist2
import pytest
import pandas as pd
import numpy as np
import sys
import os

def test_Zipdist2():
	class X():
		def __init__(self, name):
			self.name = name

	x = X(name = 'examplezip2')
	x.year = 2020
	x.exnp = np.zeros(3)
	x.expd = pd.DataFrame({"A":[1,2,3], "B":[2,4,6]})

	z = Zipdist2(name = "examplezip2", target = x)
	assert z.target is x


	z._save(dest = "xxx", dest_tar = "xxx.tar.gz")
	assert os.path.isfile("xxx.tar.gz")

	x2 = X(name = 'examplezip2')
	assert 'year' not in x2.__dict__.keys()
	z._build(target = x2, dest = "xxx", dest_tar = "xxx.tar.gz")
	assert np.all(x2.exnp == x.exnp)
	assert np.all(x2.expd == x.expd)
	assert np.all(x2.name == x.name)
	assert np.all(x2.year == x.year)

def test_cleanups():
	""" Adds cleanup of folders and .tar.gz files produced during testing"""
	os.system(f"rm -rf xxx")
	os.system(f"rm xxx.tar.gz")