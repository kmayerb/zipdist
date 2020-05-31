# zipdist

Keeping numpy and pandas attributes of python classes nice and tidy

[![Build Status](https://travis-ci.com/kmayerb/zipdist.svg?branch=master)](https://travis-ci.com/kmayerb/zipdist)


## Example

Suppose you have a Python class Skinner.
You load it up with two attributes:

* `bart` a basic numpy array of zeros, and 
* `lisa` a smart pandas DataFrame

Because Y inherits methods from the parent Zipdist (in particular 
`_save()`, and `_build()`, you can archive the non-json serializable attributes 
of your class, and rebuild the attributes from the original 
instance directly from `Simpsons.tar.gz`.

As an added benefit, the .tar.gz provides a tiddy human readable 
record of your python class attributes as .csv files, 
which you can port on over to R, Excel, Julia, or Matlab.



```python

from zipdist.zip import Zipdist
import pandas as pd
import numpy as np
import sys
import os

class Skinner(Zipdist):
	def __init__(self, name):
		self.name = name
		self.year = None

# here you have an <Willy> and instance of the class Skinner.
Willy= Skinner(name ='Simpsons')
Willy.years = [2020,2019]
Willy.bart = np.zeros(10)
Willy.lisa = pd.DataFrame([{"Pi":3.1415,"e":2.7182}])
Willy._save(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
assert os.path.isfile("Simpsons.tar.gz")

# Create a new instance, Chalmers. It has no attributes 'bart' or 'lisa'
Chalmers = Skinner("Simpsons")
assert 'bart' not in Chalmers.__dict__.keys()
assert 'years' not in Chalmers.__dict__.keys()

# But you can rebuilt the attributes from Willy directly from a archived .tar.gz file
Chalmers._build(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
assert isinstance(Chalmers.bart, np.ndarray)
assert isinstance(Chalmers.lisa, pd.DataFrame)

```

Here is what Zipdist does

```bash
Saving bart to .csv : Simpsons/bart.cs
Saving lisa to .csv : Simpsons/lisa.csv
Saving JSON with complex attribute definitions : Simpsons/complex_attributes.json
Saving JSON with simple attribute definitions : Simpsons/simple_attributes.json
Combining saved files in : [Simpsons.tar.gz].
Contents of Simpsons.tar.gz :
	Simpsons
	Simpsons/bart.cs
	Simpsons/complex_attributes.json
	Simpsons/lisa.csv
	Simpsons/simple_attributes.json
setting simple attribute name to Simpsons
setting simple attribute years to [2020, 2019]
setting [csv] to [np.ndarray] for attribute bart from: Simpsons/bart.cs
setting [csv] to [pd.DataFrame] for attribute lisa from: Simpsons/lisa.csv
```
