from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(48.865070, 2.380009, 40.4168, 3.7038)) == float
    assert (haversine(48.865070, 2.380009, 40.4168, 3.7038)) == 945.1838268692153
