from pytest import raises, approx

def test_float():
    assert (0.1 + 0.2) == approx(0.3)

def test_exception():
    with raises(ValueError):
        raise ValueError
