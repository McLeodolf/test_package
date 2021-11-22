import test_package
from test_package.lib import try_me

def test_tryme():
    assert type(try_me()) == str
