# zipdist

Keeping NumPy and Pandas attributes of python classes nice and tidy

[![Build Status](https://travis-ci.com/kmayerb/zipdist.svg?branch=master)](https://travis-ci.com/kmayerb/zipdist)
[![Coverage Status](https://coveralls.io/repos/github/kmayerb/zipdist/badge.svg?branch=master)](https://coveralls.io/github/kmayerb/zipdist?branch=master)
[![PyPI version](https://badge.fury.io/py/zipdist.svg)](https://badge.fury.io/py/zipdist)

The Zipdist2 class provides methods for saving and reloading NumPy arrays and Pandas DataFrame object attributes.

Complex attributes are saved to a single `.tar.gz` file.

The contents of the `.tar.gz` provides a tidy human-readable record of Pandas and Numpy Python class attributes as .csv and binary files. 

## Install

```
pip install zipdist==0.1.3
```


## Basic Example

```python
from zipdist.zip2 import Zipdist2
import pandas as pd
import numpy as np
import os

class X():
	def __init__(self, name):
		self.name = name

x = X(name = 'example_target_object')
x.example_simple_attr = [1989, 2020]
x.example_np_attr = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
x.example_pd_attr  = pd.DataFrame({"A":[1,2,3], "B":[2,4,6]})

z = Zipdist2(name = "zipper", target = x)
z._save(dest = "archive", dest_tar = "archive.tar.gz")
assert os.path.isfile("archive.tar.gz")
```

```
Saving example_np_attr to .csv : archive/example_np_attr.csv
Saving example_np_attr to .npy : archive/example_np_attr.npy
Saving example_pd_attr to .csv : archive/example_pd_attr.csv
Saving example_pd_attr to .feather : archive/example_pd_attr.feather
Saving JSON with complex attribute definitions : archive/complex_attributes.json
Saving JSON with simple attribute definitions : archive/simple_attributes.json
Combining saved files in : [archive.tar.gz].
```



### Contents of archive.tar.gz

```
archive
├── complex_attributes.json
├── example_np_attr.csv
├── example_np_attr.npy
├── example_pd_attr.csv
├── example_pd_attr.feather
└── simple_attributes.json
```

### Reload All Attributes of a Target Object with `._build()`

```python
x_new = X(name = 'example_target_object')
z = Zipdist2(name = "zipper", target = x_new)
# You can use the z._build() and reload all object attributes
z._build(target = x_new, dest = "archive", dest_tar = "archive.tar.gz")
```

```
Setting simple attribute name to example_target_object
Setting simple attribute example_simple_attr to [1989, 2020]
Setting [npy] to [np.ndarray] for attribute example_np_attr from: example_np_attr.npy
Setting [feather] to [pd.DataFrame] for attribute example_pd_attr from: example_pd_attr.feather
```

For instance:

``` ipython
>>>	x_new.example_simple_attr:
[1989, 2020]
>>>	x_new.example_np_attr:
[[0 1 2 3]
 [4 5 6 7]]
>>>	x_new.example_pd_attr:
   A  B
0  1  2
1  2  4
2  3  6
```

### Reload Simple and Complex Object Attributes One by One with `._ready()`, `_reload_simple()`, and `_reload_complex()`.


```python
# You can alternatively use the z._ready() and reload object attributes one by one
x_new = X(name = 'example_target_object')
z = Zipdist2(name = "zipper", target = x_new)
z._ready(target = x_new, dest = "archive", dest_tar = "archive.tar.gz")
z._reload_complex(k='example_np_attr')
z._reload_simple(k='example_simple_attr')
```
