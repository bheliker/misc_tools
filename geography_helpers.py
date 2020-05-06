def haversine(point1, point2):
    """Returns the distance between two [lat,lon] points, in km"""
    
    R = 6373.0    #radius of the Earth in km

    lat1 = math.radians(point1[0])
    lon1 = math.radians(point1[1])
    lat2 = math.radians(point2[0])
    lon2 = math.radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    #Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c #in km
    
    return(distance)

def km_miles(km):
    miles = km*0.62137119223733
    return miles

def miles_km(miles):
    km = miles*1.609344
    return km

def rad_deg(angle_radians):
    angle_degrees=(180/math.pi)*angle_radians 
    return angle_degrees

def deg_rad(angle_degrees):
    angle_radians=(math.pi/180)*angle_degrees
    return angle_radians

def point_from_raddist(lat,lon,distance_km,deg):
    """
    A point {lat,lon} is a distance distance_km out on the deg radial (degrees) from point
    0 deg is North, 90 is W, 180 is S, 270 is E
    from: http://www.edwilliams.org/avform.htm#LL
    """

    radius_km = 6371.0

    tc = deg_rad(deg)
    d = distance_km/radius_km

    lat1 = deg_rad(lat)
    lon1 = deg_rad(lon)

    lat = math.asin(math.sin(lat1)*math.cos(d)+math.cos(lat1)*math.sin(d)*math.cos(tc))

    if (math.cos(lat)==0):
        lon=lon1
    else:
        lon=((lon1 - math.asin(math.sin(tc)*math.sin(d)/math.cos(lat))+math.pi) % (2*(math.pi)))-math.pi

    return(rad_deg(lat), rad_deg(lon))