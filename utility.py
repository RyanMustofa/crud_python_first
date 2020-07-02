import pymysql.cursors


class Test1:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        db = pymysql.connect("localhost", "root", "1973", "python_db")
        self.cursor = db.cursor()
        self.db = db

    def selectAll(self):
        if(len(self.id) == 0):
            print("please insert")
            return "none"
        elif(len(self.id) > 0):
            if(int(self.id) > 0):
                sql = "SELECT * FROM test1 WHERE id= %s" % self.id
                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                    return self.cursor.fetchall()
                except:
                    self.db.rollback()
                    return False
            else:
                sql = "SELECT * FROM test1"
                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                    return self.cursor.fetchall()
                except:
                    self.db.rollback()
                    return False
    
    def insert(self):
        sql = (
            "INSERT INTO test1 (first_name,last_name) VALUES ('%s','%s')"
            %
            (self.first_name, self.last_name)
        )
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def update(self):
        sql = (
            "UPDATE test1 SET first_name='%s' , last_name='%s' WHERE id='%s'"
            %
            (self.first_name, self.last_name, self.id)
        )
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def delete(self):
        sql = "DELETE FROM test1 WHERE id='%s'" % self.id
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
