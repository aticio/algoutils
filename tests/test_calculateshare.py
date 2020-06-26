import algoutils

def test_calculate_share():
    share = algoutils.calculate_share(100000, 1.2, 120, 0.02)
    print(share)

    assert share is not None