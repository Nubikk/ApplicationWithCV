import sqlite3

#conn = sqlite3.connect('DB.sqlite')

#cur = conn.cursor()
#cur.execute("INSERT INTO Logins(login) VALUES('aaa');")
#cursor = conn.execute('''select * from Logins''')
#print(cursor.fetchall())

def add(lgn,pass_word,lkn):
    conn = sqlite3.connect('DB.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO Logins(login) VALUES('{}');".format(lgn))
    conn.commit()
    cur.execute("INSERT INTO Passwords(password) VALUES('{}');".format(pass_word))
    conn.commit()
    cur.execute("INSERT INTO Links(link) VALUES('{}');".format(lkn))
    conn.commit()
    cur.execute("""INSERT INTO Generals (login_fk, password_fk, link_fk) 
                SELECT login_id,password_id,link_id FROM Logins,Passwords,Links 
                ORDER BY 
                    login_id DESC,
                    link_id DESC, 
                    password_id DESC
                LIMIT(1);""")
    conn.commit()
    conn.close()

def show(link):
    conn = sqlite3.connect('DB.sqlite')
    cur = conn.cursor()
    cur.execute("""
    Select login, password
    From Logins Join Generals ON login_id = login_fk
    Join Passwords ON password_id = password_fk 
    Join Links ON link_id = link_fk
    WHERE link = '{}'
    """.format(link))
    buffer = cur.fetchall()

    conn.commit()
    conn.close()
    return buffer[0][0],buffer[0][1]



def drop(link):
    conn = sqlite3.connect('DB.sqlite')
    cur = conn.cursor()

    cur.execute("""
     SELECT link_id FROM Links 
     WHERE link = '{}';
    """.format(link))

    buffer = cur.fetchall()
    buffer = buffer[0][0]

    cur.execute("""
    DELETE FROM Logins 
    WHERE login_id = '{}'
    """.format(buffer))
    conn.commit()

    cur.execute("""
        DELETE FROM Passwords 
        WHERE password_id = '{}'
        """.format(buffer))
    conn.commit()

    cur.execute("""
        DELETE FROM Links 
        WHERE link_id = '{}'
        """.format(buffer))
    conn.commit()
    conn.close()


