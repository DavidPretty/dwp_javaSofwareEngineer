import mysite.geo as geo

def test_get_haversine_distance_greater_than_50_miles():
    assert(geo.get_haversine(50, 0, 51, 0) > 50)

def test_get_haversine_distance_less_than_50_miles():
    assert(geo.get_haversine(50, 0, 50.5, 0) < 50)

def test_is_within_50_miles_of_London_returns_true_for_within_50_miles_lat_long():
    assert geo.is_within_50_miles_of_London(51.35527,-0.13472)

def test_is_within_50_miles_of_London_returns_false_for_outside_50_miles_lat_long():
    assert not geo.is_within_50_miles_of_London(52.39312, 0.72292)
