# import mysql.connector
class DBManager:
    def __init__(self,host,user,password,database):
        self.mysql_connection = mysql.connector.connect(host=host,user=user,password=password,database=database)
        self.cursor = self.mysql_connection.cursor()
    def get_data(self,table_name,data_name = ["*"]):
        get_data_str = ",".join(data_name)
        self.cursor.execute(f"SELECT {get_data_str} FROM {table_name}")
        a = self.cursor.fetchall()
        return a
class tool:
    def __init__(self):
        print("creat tool")
    def string_to_list(self,string,c = ","):
        return list(string.split(c))