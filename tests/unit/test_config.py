from nordpoolapi import NordPoolClass

def test_config():
    nordPoolAPI = NordPoolClass()
    
    assert nordPoolAPI.username is not None, "User missing from environment or .env file"
    assert nordPoolAPI.subKey is not None, "Subscription key missing from environment or .env file"
    assert nordPoolAPI.password is not None, "Password missing from environment or .env file"