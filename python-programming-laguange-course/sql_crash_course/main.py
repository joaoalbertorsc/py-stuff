from database import cursor,db


def add_log(text,user):
    sql = ("""
        insert into logs(text, user)
        values (%s, %s) 
        """)
    cursor.execute(sql,(text,user))
    db.commit()
    log_id = cursor.lastrowid
    print(f"Added log {log_id}")


def get_logs(table):
    sql = f"""
        select *
        from {table}
        order by created desc
    """
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[1])


def update_log(table,text,user):
    sql = (f"""
        update {table}
        set text = %s
        where id = %s 
        """)
    cursor.execute(sql,(text,user))
    db.commit()
    print(f"{table} UPDATED!")


def delete_log(table,id):
    sql = (f"""
        delete 
        from {table}
        where id = %s 
        """)
    cursor.execute(sql,(id,))
    db.commit()
    print(f"log wich id = {id} deleted with success!")

delete_log('logs', 2)

# update_log('logs', 'log 02', 2)

# get_logs("logs")

# add_log('log 01', 'Brad')
# add_log('log 02', 'John')
# add_log('log 03', 'Eve')
