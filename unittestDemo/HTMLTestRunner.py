import pytest

data1 = ['zheng', 'ji', 'chuan']


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收传入的参数，接收一个参数
    user = request.param
    print("\n打开用户首页准备登录，登录的用户名为：%s" % user)
    return user


@pytest.mark.parametrize('data', data1)
def test_data(data):
    print(data)


if __name__ == '__main__':
    pytest.main()
