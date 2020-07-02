import pymysql.cursors

db = pymysql.connect("localhost","root","1973","python_db")
cursor = db.cursor()
sql = """CREATE TABLE test1(
        id INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        PRIMARY KEY(id)
    )"""
cursor.execute(sql)
db.close()
