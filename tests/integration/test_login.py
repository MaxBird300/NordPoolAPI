import pytest
from nordpoolapi import NordPoolClass

@pytest.mark.integration
def test_login():
    nordPoolAPI = NordPoolClass()
    nordPoolAPI.authenticateUser()
