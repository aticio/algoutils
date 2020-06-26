import algoutils

def test_get_current_timestamp():
    timestamp = algoutils.get_current_timestamp()
    print(timestamp)

    assert timestamp is not None