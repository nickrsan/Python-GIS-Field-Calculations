def get_severity(intensity, burn_rate):
	severities = { 1: “Minimal”, 2: “Low”,
					3: “Medium”, 4:”High”,
					5:”Extreme”}
	base_severity = intensity + burn_rate
	
	if base_severity > 5:
		base_severity = 5
		
	return severities[base_severity]
	
get_severity(!INTENSITY!, !BURN_RATE!)

get_severity(2, 1)
get_severity(2, 2)
get_severity(1, 1)
get_severity(1, 4)
get_severity(5, 1)