from sample_python_lib import my_functions

def test_haversine():
    # Amsterdam to Berlin
    assert my_functions.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291