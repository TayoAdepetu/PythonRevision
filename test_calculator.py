from Calculator import squared

# WARNING: The scripts py.test.exe and pytest.exe are installed in 'C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

def main():
    test_positive()
    test_negative()
    test_zero()


def test_positive():
    assert squared(2) == 4
    assert squared(3) == 9

def test_negative():
    
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    
    assert squared(0) == 0

if __name__ == "__main__":
    main()