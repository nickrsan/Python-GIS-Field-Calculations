# Python for Field Calculations

## Getting to know everyone
1. Introduce self, experience, etc
2. See who is using QGIS and ArcGIS
	- Note that this will be a bit of an experiment because the two GIS packages are just slightly different, but the Python core
	is fundamentally the same. We'll demo little parts that are specific to each package, but otherwise will run the same code.
3. Ask about experience in Python or other programming languages

## Getting started
1. Quick tour of Python in ArcGIS - note that it's not the only way to use it
	- Python window for exploring, Field Calculator for quick modifications
2. Quick tour of Python in QGIS
	- Python console - note that by default it's maybe a little less helpful than ArcGIS', but
	that the Code Editor is a nice feature that is very helpful. Also Field Calculator for quick mods again

##
1. Intro to field calculator by making a HUC4 field
	- Describe HUCs and their nested identifier and set up problem.
	- demonstrate slicing on python command line - it's easy and simple
	- then show how to fill the HUC 4 values in ArcGIS with the same slicing syntax - note the !s around field names
	- then show how in QGIS it gets more complicated than that - because their field calculator doesn't use Python directly, but
		we can make it use Python with the power of functions.
	- introduce making script files
		- make a function named truncate - takes a string and how long to make it - we'll then have it return the Python slice
		- save and load
		- Note the preview and run the calculation
		- Also show the calculation bar for quick calculations - use the substr function there
		
1. Intro to field calculator by splitting features into two random groups
	- Use this to show basics without a function, then incorporate it into a function - we'll then use it to assign many features
		later to demonstrate how GIS will run code for any number of features
		
	```
		>>> import random
		>>> random.seed(20190212)
		>>> random.random()
		0.5710417122537211
		>>> cohort = 0
		>>> random_value = random.random()
		>>> random_value
		0.6873604526423102
		>>> if random_value < 0.5:
		...     cohort = 1
		... else:
		...     cohort = 2
		...     
		>>> cohort
		2
	```
	
	Then make it into a function:
	```
		>>> def get_cohort():
		...     if random.random() < 0.5:
		...         return 1
		...     else:
		...         return 2
		...         
		>>> get_cohort()
		2
	```
	Note that we don't need to store any of these values - we can use `random.random()` directly in our comparison, and the use
	of `return` which tells the function what to send back to the `caller` - or whatever code told it to run, which usually wants
	a value. This becomes important with field calculations.
	
## Calculating some fields
1. Take code from previous section and turn it into a field calculation. In ArcGIS, we'll add the field first - in QGIS, we'll do
	it from the field calculator dialog. 
	
## With more time
1. Addresses - turn them into strings - see address_snippets.py
2. Meadows - run the high elevation/high flow code  - see meadows_snippets.py
