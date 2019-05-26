import pytest

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print('Setting up pytest Session')

@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print('Setting up Module')

@pytest.fixture(scope='class', autouse=True)
def setup_class():
    print('Setting up class')

@pytest.fixture(scope='function')
def setup_function():
    print('Setting up function')

@pytest.fixture(scope='function', params=[1,2])
def setup_function(request):
    print('Setting up function')
    return request.param

@pytest.mark.usefixtures('setup_function')
def test_with_param(setup_function):
    print('value passed {}'.format(setup_function))
    assert True

class TestClass:
    def test_it(self):
        assert True
