import psycopg2
import boto3
load.dotenv()
password = AWS_PASSWORD
port = AWS_PORT
host= AWS_HOST
username= AWS_USERNAME
database= AWS_DATABASE
conn = None
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password,
        sslmode='verify-full',
    sslrootcert='/certs/global-bundle.pem'
    )
    cur = conn.cursor()
    cur.execute('SELECT version();')
    print(cur.fetchone()[0])
    cur.close()
except Exception as e:
    print(f"Database error: {e}")
    raise
finally:
    if conn:
        conn.close()
