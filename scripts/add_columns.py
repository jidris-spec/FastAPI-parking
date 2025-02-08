from sqlalchemy import create_engine, text

# Update this path with your actual database file
DATABASE_URL = "sqlite:///app/db/parking.db"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(text("ALTER TABLE users ADD COLUMN reset_token TEXT;"))
    connection.execute(text("ALTER TABLE users ADD COLUMN reset_token_expiry DATETIME;"))
    connection.commit()  # Commit the changes

print("Columns added successfully.")
