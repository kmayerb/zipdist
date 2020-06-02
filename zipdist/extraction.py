import os
import tarfile
import pandas as pd
import numpy as np

class ExtractMachina():
	""" 
	Extaction Machina - return Pandas and NumPy components of .tar.gz archive 
	without extracting the file to disk.
	
	Attributes 
	----------

	Example
	-------
	em = ExtractMachina(dest_tar= "Simpsons.tar.gz")
	em.return_extracted_component(filename = 'lisa.csv', filetype = "pd.DataFrame")

	"""
	def __init__(self, dest_tar):
		self.dest_tar = dest_tar
		self.dest = dest_tar.replace(".tar.gz", "")

	def return_extracted_component(self, filename, filetype):
		"""
		filename : string
			example 'lisa.csv'
		filetype : string
			must be 'nd.nparray' or 'pd.DataFrame'

		"""
		assert filetype in ['np.ndarray','pd.DataFrame'], "filetype arg must be 'np.ndarray' or 'pd.DataFrame'"
		assert np.any([filename.endswith(extension) for extension in ['.csv', '.feather', 'npy']]), "filenames must be .csv, .feather or .npy" 
		assert os.path.isfile(self.dest_tar), f"{self.dest_tar} file does not exist"

		dest_filename = os.path.join(self.dest, filename)
		with tarfile.open(self.dest_tar) as tar:
			print(dest_filename)
			with tar.extractfile(dest_filename) as fh:
				if filetype == 'pd.DataFrame':
					if filename.endswith(".feather"):
						return pd.read_feather(fh)
					elif filename.endswith(".csv"):
						return pd.read_csv(fh)
				if filetype == 'np.ndarray':
					if filename.endswith(".npy"):
						#return np.load( file = fh) FAILS: AttributeError: '_FileInFile' object has no attribute 'fileno'
						return np.frombuffer(fh.read(), dtype='<u2')	
					elif filename.endswith(".csv"):
						return np.genfromtxt(fh, delimiter=',')






