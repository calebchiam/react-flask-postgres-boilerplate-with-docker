import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(user="calebchiam",
                                  password="90304027",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pgguide")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties

    create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table successfully created.")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if connection is not None:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
