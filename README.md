# misc_tools
Snippets and Tools I use


- `geography_helpers.py`: a small collection of geography math functions:
	- `haversine(point1, point2)`: Calculates the [great-circle distance](https://en.wikipedia.org/wiki/Haversine_formula) between two [lat,lon] points
	- `point_from_raddist(lat,lon,distance,deg)`: given a starting point, direction and distance, calculate the final point. Great for generating bounding boxes.
	- conversion formulas: quick helpers
		- `km_miles()` converts km to miles, `miles_km()` does the opposite
		- `rad_deg()` converts radians to degress and `deg_rad()` does the opposite
		
- `plotGPXfile()`: accepts a GPX file as input and returns a folium map. Intended for use in a Jupyter notebook for quickly checking GPX files.

- `kalmanFilter(data, R, Pi, Q)`: A simple [Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter)for use with basic 1-D, linear, time series sensors. Pass in an array, it returns a filtered array: `kalmanFilter(sensor1['temperatures'].values)`. 

- `flexpointsensor.py`: This script reads a [Flexpoint bend sensor](https://www.flexpoint.com) and [plots it](https://flic.kr/p/2ja6WfJ). Can be used as the basis for any analog sensor on a Serial port.
