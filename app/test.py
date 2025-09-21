from sqlalchemy import create_engine, text

# Replace with your credentials
DATABASE_URL = "mysql+pymysql://admin:admin123@localhost:3306/mydb"

# Create engine
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Connection successful:", result.scalar())
except Exception as e:
    print("❌ Connection failed:", e)