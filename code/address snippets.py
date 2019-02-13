
# Some one-liner options
!street_number! + " " + !street_name! + " #" + !unit_number! + ", " + !city! + ", " + !state! + " " + !zip!
str(!street_number!) + " " + !street_name! + " #" + str(!unit_number!) + ", " + !city! + ", " + !state! + " " + !zip!
"{num} {street} #{unit}\n{city}, {state} {zip}".format(num=!street_number!, street=!street_name!, unit=!unit_number!, city=!city!, state=!state!, zip=!zip!)



## ArcGIS
def make_address(street_number, street_name, unit, city, state, zip):
	if unit is not None and unit != "":  # if unit is not null or blank
	   unit_string = "#{}".format(unit)
	else:
		unit_string = ""
		
	address = "{num} {street} {unit}\n{city}, {state} {zip}".format(num=street_number, street=street_name, unit=unit_string, city=city, state=state, zip=zip)

	return address
	
# Call with
make_address(!street_number!, !street_name!, !unit_string!, !city!, !state!, !zip!)


## QGIS 3.x
@qgsfunction(args='auto', group='Custom')
def make_address(feature, parent):
	unit = feature.attribute('unit')
	if unit is not None and unit != "":  # if unit is not null or blank
	   unit_string = "#{}".format(unit)
	else:
		unit_string = ""
	
	street_number = feature.attribute('street_number')
	street_name = feature.attribute('street_name')
	city = feature.attribute('city')
	state = feature.attribute('state')
	zip = feature.attribute('zip')
	address = "{num} {street} {unit}\n{city}, {state} {zip}".format(num=street_number, street=street_name, unit=unit_string, city=city, state=state, zip=zip)

	return address
	
# Call with
make_address()