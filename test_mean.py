from mean import mean

# simple example with integers
def test_ints():
    num_list = [1,2,3,4,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

# when there is 0 in the list
def test_zeros():
    num_list = [1,2,0,3,4,5]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

# when the result is double, not integer
def test_floats():
    num_list = [1,2,3,5]
    obs = mean(num_list)
    exp = 2.75
    assert obs == exp

# when the result is a really large number
def test_large():
    num_list = list(range(1000000, 10000000))
    obs = mean(num_list)
    exp = 5499999.5
    assert obs == exp

# when the elements are doubles, not integers
def test_float_elems():
    num_list = [1.4,2.91238,3.0,0.9162371823,0.0]
    obs = mean(num_list)
    exp = 1.6457234364600002
    assert exp - 0.00001 < obs < exp + 0.00001

