"""Pytest playground."""
import pytest

@pytest.fixture(autouse=True)
def setup(request):
    """Set up Pytest."""
    print('setting up baby')

    def teardown():
        print('Teardown')

    request.addfinalizer(teardown)


def test1(setup):
    """First test."""
    assert True

def test2():
    """Second test."""
    assert True
