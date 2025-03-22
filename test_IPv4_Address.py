from IPv4_Address import validate
def main():
    test_LoopBack()
    test_ModemAddress()
    test_WrongAddress()

def test_LoopBack():
    assert validate("127.0.0.1") == True
    assert validate("127.0.0.0") == True

def test_ModemAddress():
    assert validate("192.168.6.1") == True
    assert validate("192.168.90.1") == True

def test_WrongAddress():
    assert validate("10.10.10.10.10") == False
    assert validate("256.0.0.1") == False
    assert validate("254.0.765.1") == False

if __name__ == "__main__":
    main()
