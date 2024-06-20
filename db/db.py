import pymysql
import sys

conn = None
cur = None

def connect() :
    global conn

    try:
        # MariaDB Connection
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

    # 조건에 맞는 상, 하의 매칭 리스트 검색 후 랜덤으로 1개 데이터 가져온다.
    # 조건 1 : 온도 범위
    # 조건 2 : 태그 (러블리, 페미닌, 스트릿, 캐주얼)
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
    
    # 매칭 결과를 스타일리스트에 저장한다.
    sql = '''insert into style_list(matching_date, temperature, clothes_top_id, clothes_bottom_id, created_date) 
            values(STR_TO_DATE("''' + machingDate + '''", "%Y-%m-%d"), "''' + str(temperature) + '''", "''' + str(top_id) + '''", "''' + str(bottoom_id) + '''", now())'''
    
    cur.execute(sql)
    conn.commit()

def getStyleList() :
    global conn, cur
    cur = conn.cursor(pymysql.cursors.DictCursor)

    # 스타일리스트 목록을 매칭날짜, 저장 날짜로 조회한다.
    # 상의, 하의 이미지를 조인해서 함꼐 조회한다.
    sql = '''select s.id, matching_date, temperature, top.image_path, bottom.image_path, created_date from style_list s
            join clothes_top top on s.clothes_top_id = top.id
            join clothes_bottom bottom on s.clothes_bottom_id = bottom.id
            order by matching_date desc, created_date asc;'''

    cur.execute(sql)
    return cur.fetchall()

def getStyleById(id) :
    global conn, cur
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql = '''select s.id, matching_date, temperature, top.image_path, top.link, bottom.image_path, bottom.link, created_date from style_list s
            join clothes_top top on s.clothes_top_id = top.id
            join clothes_bottom bottom on s.clothes_bottom_id = bottom.id
            where s.id = ''' + str(id) + '''
            order by matching_date desc, created_date asc;'''

    cur.execute(sql)
    return cur.fetchall()[0]