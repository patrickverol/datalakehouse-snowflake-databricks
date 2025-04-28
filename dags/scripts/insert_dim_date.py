import psycopg2
from datetime import date, datetime, timedelta

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="dbSource",
    user="useradmin",
    password="password",
    host="db_source",
    port="5432"
)
cur = conn.cursor()

now = datetime.now()

def insert_dim_date():
    start_date = date(2021, 1, 1)
    end_date = date(2031, 12, 31)
    current = start_date
    sks = []

    print("Starting date dimension insertion...")
    
    while current <= end_date:
        try:
            cur.execute("""
                INSERT INTO dw.dim_date (full_date, day, month, year)
                VALUES (%s, %s, %s, %s) RETURNING sk_date
            """, (
                current,
                current.day,
                current.month,
                current.year
            ))
            
            result = cur.fetchone()
            if result is not None:
                sks.append(result[0])
            
            current += timedelta(days=1)
        except psycopg2.Error as e:
            print(f"Error inserting date {current}: {e}")
            current += timedelta(days=1)
    
    # Commit the changes
    conn.commit()
    print(f"✅ Successfully inserted dates from {start_date} to {end_date}")
    
    return sks

if __name__ == "__main__":
    try:
        insert_dim_date()
    finally:
        cur.close()
        conn.close() 