import pytest
import numpy as np
import pandas as pd
from zipdist.zip2 import Zipdist2
from zipdist.extraction import ExtractMachina
import os 
import sys

def make_tar_gz():
	class X():
		def __init__(self, name):
			self.name = name

	x = X(name = 'xxx')
	x.year = 2020
	x.exnp = np.zeros(3)
	x.expd = pd.DataFrame({"A":[1,2,3], "B":[2,4,6]})
	z = Zipdist2(name = "xxx", target = x)
	z._save(dest = "xxx", dest_tar = "xxx.tar.gz")
	os.system('rm -rf xxx')
	return True

def test_extraction_on_pdDataFrame_from_csv():
	x = make_tar_gz()
	assert os.path.isfile("xxx.tar.gz")
	em = ExtractMachina(dest_tar= "xxx.tar.gz")
	r = em.return_extracted_component(filename = 'expd.csv', filetype = "pd.DataFrame")
	assert isinstance(r, pd.DataFrame)
	assert "A" in r.columns
	assert "B" in r.columns
	os.system('rm xxx.tar.gz')

def test_extraction_on_pdDataFrame_from_feather():
	x = make_tar_gz()
	assert os.path.isfile("xxx.tar.gz")
	em = ExtractMachina(dest_tar= "xxx.tar.gz")
	r = em.return_extracted_component(filename = 'expd.feather', filetype = "pd.DataFrame")
	assert isinstance(r, pd.DataFrame)
	assert "A" in r.columns
	assert "B" in r.columns
	os.system('rm xxx.tar.gz')

def test_extraction_on_np_ndarray_from_csv():
	x = make_tar_gz()
	assert os.path.isfile("xxx.tar.gz")
	em = ExtractMachina(dest_tar= "xxx.tar.gz")
	r = em.return_extracted_component(filename = 'exnp.csv', filetype = "np.ndarray")
	assert isinstance(r, np.ndarray)
	os.system('rm xxx.tar.gz')

def test_extraction_on_np_ndarray_from_npy():
	x = make_tar_gz()
	assert os.path.isfile("xxx.tar.gz")
	em = ExtractMachina(dest_tar= "xxx.tar.gz")
	r = em.return_extracted_component(filename = 'exnp.npy', filetype = "np.ndarray")
	assert isinstance(r, np.ndarray)
	os.system('rm xxx.tar.gz')





	
