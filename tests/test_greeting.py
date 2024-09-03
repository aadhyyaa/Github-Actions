import pytest
from hello import Hello

def test_greeting():
    assert Hello.hello_world() == 'Hello World'

if __name__=='__main__':
    pytest.main()