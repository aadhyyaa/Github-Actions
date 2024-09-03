import pytest
from main import Hello

def test_ans():
    assert Hello.ans() == 'New Delhi'

if __name__=='__main__':
    pytest.main()