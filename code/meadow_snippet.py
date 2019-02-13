
## ArcGIS Version
def classify_meadow(catchment_area, elevation):  # provide area and elevation as direct arguments to the function
    elevation_classification = None  # make sure we define the variables - we can skip this, but it's good practice for more complicated conditionals
    if elevation > 2500:  # check if the elevation is higher than 2500
        elevation_classification = "High altitude"  # if so, call it high altitude
    else:  # otherwise
        elevation_classification = "Low altitude"  # call it low altitude instead

    catchment_classification = None
    if catchment_area > 1000000:
        catchment_classification = "High flow"
    else:
        catchment_classification = "Low flow"

    classification = "{}, {}".format(elevation_classification, catchment_classification)

    return classification
	

## QGIS 3 version
@qgsfunction(args='auto', group='Custom')
def classify_meadow(feature, parent):
    elevation_classification = None
    if feature.attribute('ELEV_MEAN') > 2500:  # in QGIS, we don't need to pass arguments for each value because we can access the feature directly
        elevation_classification = "High altitude"
    else:
        elevation_classification = "Low altitude"

    catchment_classification = None
    if feature.attribute('CATCHMENT_AREA') > 1000000:  # area in square meters == 10 square km
        catchment_classification = "High flow"
    else:
        catchment_classification = "Low flow"

    classification = "{}, {}".format(elevation_classification, catchment_classification)  # combine the elevation classification and catchment classification into a single string

    return classification  # return the value to the caller