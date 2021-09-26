from oracle.oracle import MyOracle
from pytest_mock import MockerFixture
import pytest
import cx_Oracle


def test_get_DB_version():
    myoracle = MyOracle('SYSTEM', '', '192.168.18.130:1521/orclcdb')
    assert myoracle.get_DB_version() == '19.3.0.0.0'



# @pytest.mark.parametrize('test_input,expected', [('TEST001', ('TEST001', )),
#                                                  ('TEST002', None)])
# def test_select_table(mocker, test_input, expected):
#     myoracle = MyOracle('SYSTEM', '', '192.168.18.130:1521/orclcdb')
# #     assert myoracle.select_table('TEST001') == ('TEST001',)
# #     assert myoracle.select_table('TEST000') == None
# #     moke_value = {'self.cursor.execute': '', 'self.cursor.fetchone': ('TEST0002',)}
# #     myoracle.select_table = mocker.patch.object(MyOracle, 'select_table', return_value = expected)
# #     mocker.patch('oracle.oracle.MyOracle.__init__', return_value = ('TEST002', ))
# #     mocker.patch('cx_Oracle.connect', return_value = ('TEST002', ))
# #     mocker.patch('cx_Oracle.Cursor', return_value = ('TEST002', ))
#     actual = myoracle.select_table(test_input)
#     assert actual == expected
    
# def test_select_table_excpet():
#     myoracle = MyOracle('SYSTEM', '', '192.168.18.130:1521/orclcdb')
#     with pytest.raises(cx_Oracle.DatabaseError) as e:
#         myoracle.select_table('\'')
#     actual = e.value.args[0].code
#     assert actual == 1756