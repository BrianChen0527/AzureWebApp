from types import TracebackType
import psycopg2


class connection():
    def __init__ (self):
        self.host = "calcdb.postgres.database.azure.com"
        self.dbname = "postgres"
        self.user = "brian"
        self.password = "Clone112424!"
        self.sslmode = "require"
        self.conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(self.host, self.user, self.dbname, self.password, self.sslmode)
        self.conn = psycopg2.connect(self.conn_string) 
        self.conn.autocommit = True
        print("Connection established")
        self.cursor = self.conn.cursor()
        # Drop previous table of same name if one exists
        self.cursor.execute("DROP TABLE IF EXISTS inventory;")
        print("Finished dropping table (if existed)")
        self.cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, request_str VARCHAR(50), num1 INTEGER, num2 INTEGER, res INTEGER);")
        print("Finished creating table")

    def insert_data(self, request_str, num1, num2, res):
        self.cursor.execute("INSERT INTO inventory (request_str, num1, num2, res) VALUES (\'%s\', %d, %d, %d);" % (str(request_str), int(num1), int(num2), int(res)))
        print("Inserted 1 row of data")

    def select_data(self):
        self.cursor.execute("select * from inventory order by id desc limit 5;")
        rows = self.cursor.fetchall()
        return rows
       
    # Clean up
    def __del__(self):
        print("cleaning up")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
