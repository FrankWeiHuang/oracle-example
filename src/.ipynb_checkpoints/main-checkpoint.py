from oracle.oracle import MyOracle

if __name__ == '__main__':
    try:
        myoracle = MyOracle('SYSTEM', '', '192.168.18.130:1521/orclcdb')
        print(myoracle.get_DB_version())
#         print(myoracle.create_table('SYSTEM', 'test001', """
#             person_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
#             first_name VARCHAR2(50) NOT NULL,
#             last_name VARCHAR2(50) NOT NULL,
#             PRIMARY KEY(person_id)
#         """))
        print(myoracle.select_table('\''))
    except Exception as e:
        print('main excpet: ')
        print(e)