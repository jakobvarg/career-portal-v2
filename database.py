# we are import os as we are storing the database connection string as secret  
# as we are storing this code in github in public repository it is not safe 
import psycopg2.extras
import os

# Connection string
conn_string = os.environ["DB_CONN_STR"]

def load_jobs_from_db():
    try:
        # Open a new connection for each request
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        sql = "SELECT * FROM jobs;"
        cursor.execute(sql)
        results = cursor.fetchall()

        # Close cursor and connection after fetching data
        cursor.close()
        conn.close()

        return results

    except Exception as ex:
        print(f"Database error: {ex}")
        return []

