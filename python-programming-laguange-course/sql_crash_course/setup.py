import mysql.connector
from mysql.connector import errorcode

from sql_crash_course.database import cursor,db

DB_name = 'crash_course'

TABLES = {}

TABLES['logs'] = f"""
    use {DB_name};
    create table `logs` (
    `id` int(11) not null auto_increment,
    `text` varchar(250) not null,
    `user` varchar(250) not null,
    `created` datetime not null default current_timestamp,
    primary key (`id`)
    ) engine=InnoDB;
"""



def create_DB():
    cursor.execute(f"create database if not exists {DB_name}")
    print(f"DB {DB_name} created!")


def create_table():
    cursor.execute(f"USE {DB_name}")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f"Creating table({table_name}) ",end = "")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)

create_DB()
create_table()

