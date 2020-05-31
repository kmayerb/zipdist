# zipdist

Keeping NumPy and Pandas attributes of python classes nice and tidy

[![Build Status](https://travis-ci.com/kmayerb/zipdist.svg?branch=master)](https://travis-ci.com/kmayerb/zipdist)
[![Coverage Status](https://coveralls.io/repos/github/kmayerb/zipdist/badge.svg?branch=master)](https://coveralls.io/github/kmayerb/zipdist?branch=master)


The Zipdist parent class provides methods to classes for saving
NumPy arrays and Pandas DataFrame object attributes in a single 
`.tar.gz` file and reloading those attributes back into a newinstance. 

As an added benefit, the `.tar.gz` provides a tidy human-readable 
record of your Python class attributes as .csv files, 
which you can port on over to another platform like 
R, Excel, Julia, or Matlab.

## Install

```
pip install zipdist
```


## Basic Example

``` python
from zipdist.zip import Zipdist
import pandas as pd
import numpy as np
import sys

class Y(Zipdist):
	def __init__(self, name):
		self.name = name
		self.year = None

y = Y(name ='Simpsons')
y.years = [1989, 2020]
y.bart = np.zeros(10)
y.lisa = pd.DataFrame([{"Pi":3.1415,"e":2.7182}])
y._save(dest="Simpsons", dest_tar = "Simpsons.tar.gz")


ynew = Y(name = "Simpsons")
ynew._build(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
sys.stdout.write(f"ynew.years: {ynew.years}\n")
sys.stdout.write(f"ynew.lisa:\n{ynew.lisa}\n")
sys.stdout.write(f"ynew.bart: {ynew.bart}\n")
```

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

```
ynew.years: [1989, 2020]
ynew.lisa:
       Pi       e
0  3.1415  2.7182
ynew.bart: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

## Explanation 


```python
from zipdist.zip import Zipdist
import pandas as pd
import numpy as np
import sys
import os
```

Suppose you have some class `Y`. Let it inherit methods from Zipdist

```
class Y(Zipdist):
	def __init__(self, name):
		self.name = name
		self.year = None
```

Say you instantiate an instance of `Y`, assigning it two new complex attributes:

* `bart` a basic numpy array of zeros, and 
* `lisa` a smart pandas DataFrame

```python
y = Y(name ='Simpsons')
y.years = [1989, 2020]
y.bart = np.zeros(10)
y.lisa = pd.DataFrame([{"Pi":3.1415,"e":2.7182}])
```

### `_save()`

Because Y inherits methods from the parent Zipdist (in particular 
`_save()`, and `_build()`, you can archive the non-json serializable attributes 
of your class, and rebuild the attributes from the original 
instance directly from `Simpsons.tar.gz`.

```python
# ._save creates the file Simpsons.tar.gz
y._save(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
assert os.path.isfile("Simpsons.tar.gz")
```

### `_build()` 

Suppose you want to rebuild the instance. (Note, it has no attributes `bart` or `lisa`)

```
ynew = Y("Simpsons")
assert 'bart' not in ynew.__dict__.keys()
assert 'years' not in ynew.__dict__.keys()
```
But you can rebuilt the attributes from Willy directly from a archived .tar.gz file
``` python
ynew._build(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
assert isinstance(ynew.bart, np.ndarray)
assert isinstance(ynex.lisa, pd.DataFrame)
```

### `_ready()`

You can also add simple (i.e., json serializable) or complex (numpy and panadas attributes) one by one as desired with `_ready()`
and `_reload_complex()` and `_reload_simple('years')`

```python
ynew = Y("Simpsons")
assert 'lisa' not in ynew.__dict__.keys()
assert 'bart' not in ynew.__dict__.keys()
assert 'years' not in ynew.__dict__.keys()
ynew._ready(dest="Simpsons", dest_tar = "Simpsons.tar.gz")
ynew._reload_complex('lisa')
assert isinstance(ynew.lisa, pd.DataFrame)
ynew._reload_simple('years')
assert isinstance(ynew.years, list)
```

