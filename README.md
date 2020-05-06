# misc_tools
Snippets and Tools I use


- `geography_helpers.py`: a small collection of geography math functions:
	- `haversine(point1, point2)`: Calculates the [great-circle distance](https://en.wikipedia.org/wiki/Haversine_formula) between two [lat,lon] points
	- `point_from_raddist(lat,lon,distance,deg)`: given a starting point, direction and distance, calculate the final point. Great for generating bounding boxes.
	- conversion formulas: quick helpers
		- `km_miles()` converts km to miles, `miles_km()` does the opposite
		- `rad_deg()` converts radians to degress and `deg_rad()` does the opposite