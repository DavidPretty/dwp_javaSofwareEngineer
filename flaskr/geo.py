from math import radians, sin, cos, sqrt, asin


def get_haversine(latX, lonX, latY, lonY):
    R = 3958.8  # Earth's radius in miles

    diffLat = radians(latY - latX)
    diffLon = radians(lonY - lonX)
    latX = radians(latX)
    latY = radians(latY)

    a = sin(diffLat / 2)**2 + cos(latX) * cos(latY) * sin(diffLon / 2)**2
    c = 2 * asin(sqrt(a))

    return R * c

def is_within_50_miles_of_London(latX, lonX):
    LONDON_LAT = 51.50868648029151 #Trafalgar Square
    LONDON_LONG = -0.1276495 #Trafalgar Square

    return get_haversine(latX, lonX, LONDON_LAT, LONDON_LONG) <= 50