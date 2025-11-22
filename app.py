import time
import psycopg2
import sys

def main():
    print("Starting application...")
    print("Waiting 10 seconds before attempting database connection...")
    time.sleep(10)
    
    print("Attempting to connect to database...")
    
    try:
        # Intentionally using incorrect database credentials to cause a failure
        connection = psycopg2.connect(
            host="nonexistent-database-host",
            port=5432,
            database="test_db",
            user="test_user",
            password="test_password",
            connect_timeout=5
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Database version: {db_version}")
        
        cursor.close()
        connection.close()
        
    except psycopg2.OperationalError as e:
        print(f"ERROR: Failed to connect to database!")
        print(f"Details: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error occurred!")
        print(f"Details: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
