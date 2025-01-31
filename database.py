# from sqlalchemy import 
# for now i think sqlalchemy is not required when using psycopg2. will reconfirm later on.
import psycopg2

# declare the connection string specifying
# the host name database name user name 
# and password
conn_string = "host='ep-dark-frost-a8brsyoj-pooler.eastus2.azure.neon.tech' dbname='careerportal'\
user='neondb_owner' password='npg_LRxrayB0AQI5'"

try:
  # use connect function to establish the connection
  conn = psycopg2.connect(conn_string)
  with conn:
      print('Successfully connected to the PostgreSQL database')
      with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        records = cursor.fetchall()

      print("type(records): ", type(records))
      print()
      for record in records:
        print(records,"\n")
        print("type(record): ", type(record))
        print()
except Exception as ex:
  print(f'Sorry failed to connect: {ex}')

finally:
  # First check if conn is defined like in case something is wrong in the connection string
  #dont want users to see the error
  if 'conn' in globals():
    # Close the connection if open
    if conn:
        conn.close()
        print('Connection closed')
  else:
    print('Conn is not available or not defined, so connection not open')
