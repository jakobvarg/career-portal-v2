# from sqlalchemy import
# for now i think sqlalchemy is not required when using psycopg2.extras will reconfirm later on.
# psycopg2.extras is specifically used to result result from table as a dictionary else for a list or tuple psycopg2 is only required
import psycopg2.extras
import os

# declare the connection string specifying
# the host name database name user name 
# and password
conn_string = os.environ["DB_CONN_STR"]

try:
  # use connect function to establish the connection
  conn = psycopg2.connect(conn_string)

  with conn:
    print('Successfully connected to the PostgreSQL database')
  #   #The syntax below ensures result from table jobs is a dictionary 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) 
    sql = "SELECT * FROM jobs;"
    cursor.execute(sql) 
    results = cursor.fetchall() 
    for row in results: 
      print("Job Title: {}".format(row['title'])) 
      print("Location: {}".format(row['location'])) 
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
