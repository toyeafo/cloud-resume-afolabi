from lambda_function import lambda_handler
from unittest.mock import MagicMock
from types import *
import pytest

def lambda_event():
        return {
            'Key': 'value'
        }

@pytest.fixture
def mock_context():
        return MagicMock()


def test_lambda_handler_with_mock(mock_context):

        result = lambda_handler(lambda_event, mock_context)

        assert type(result) is str
        assert isinstance(int(result), int)

if __name__=='__main__':
        pytest.main()