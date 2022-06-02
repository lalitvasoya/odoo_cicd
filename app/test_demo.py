from demo import add

def test_add():
    assert add(2, 3) == 5
    print('Works perfectly!')


if __name__ == '__main__':
    test_add()
