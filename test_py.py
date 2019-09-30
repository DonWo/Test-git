#coding:utf-8
import pytest
@pytest.mark.parametrize("test_input,expected",[ ("3+5", 8),("2+4", 6),("6 * 9", 42),])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main(["-n 2","-q","-s","test_py.py"])

# import mock
# import unittest

# class Count():
#     def add(self,a,b):
#         return a + b

# class TestCase(unittest.TestCase):
#     def test_add_mock(self):
#         '''模拟接口调用'''
#         count = Count()                             # 实例化类对象
#         count.add = mock.Mock(return_value=13)      # 模拟返回值
#         result = count.add(8,5)                     # 接口调用正确函数
#         self.assertEqual(result,13)
#         print("测试成功")

#     def test_add_success(self):
#         '''正常接口调用'''
#         count = Count()
#         # side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value
#         count.add = mock.Mock(return_value=13,side_effect=count.add)
#         result = count.add(8,8)
#         print(result)
#         # 检查mock方法是否获得了正确的参数
#         count.add.assert_called_with(8,8)
#         self.assertEqual(result,16)

# if __name__ == '__main__':
#     unittest.main()
print("123")
print("123")
print("123")
print("123")
print("123")
print("456")
print("7788")