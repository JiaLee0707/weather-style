import pymysql
import sys

conn = None
cur = None

def connect() :
    global conn

    try:
        conn = pymysql.connect(
            user="root",
            password="1234",
            host="localhost",
            port=3306,
            database="weather-style"
        )
    except pymysql.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def getRandomStyle(temperature, tag) :
    global conn, cur
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql = '''select * from clothes_top top 
            join clothes_bottom bottom on top.id = bottom.clothes_top_id
            where top.temperature_start <= ''' + str(temperature) + ''' and top.temperature_end >= ''' + str(temperature) + ''' and top.tag like "''' + tag + '''"
            and bottom.temperature_start <= ''' + str(temperature) + ''' and bottom.temperature_end >= ''' + str(temperature) + ''' and bottom.tag like "''' + tag + '''"
            order by rand() limit 1;'''

    cur.execute(sql)
    return cur.fetchall()

def saveMachingStyle(machingDate, temperature, top_id, bottoom_id) :
    global conn, cur
    cur = conn.cursor()
    
    sql = '''insert into style_list(matching_date, temperature, clothes_top_id, clothes_bottom_id, created_date) 
            values(STR_TO_DATE("''' + machingDate + '''", "%Y-%m-%d"), "''' + str(temperature) + '''", "''' + str(top_id) + '''", "''' + str(bottoom_id) + '''", now())'''
    
    cur.execute(sql)
    conn.commit()

def getStyleList() :
    global conn, cur
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql = '''select matching_date, temperature, top.image_path, bottom.image_path, created_date from style_list s
            join clothes_top top on s.clothes_top_id = top.id
            join clothes_bottom bottom on s.clothes_bottom_id = bottom.id
            order by matching_date desc, created_date asc;'''

    cur.execute(sql)
    return cur.fetchall()
