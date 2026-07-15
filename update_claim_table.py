"""
=========================================================
        UPDATE CLAIM TABLE FOR AI FRAUD DETECTION
=========================================================
"""

import sqlite3

DATABASE = "instance/healthcare.db"

connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()

cursor.execute("PRAGMA table_info(claims)")

columns = [column[1] for column in cursor.fetchall()]

new_columns = [

    ("predicted_risk", "REAL DEFAULT 0"),

    ("risk_level", "TEXT DEFAULT 'Not Predicted'"),

    ("duplicate_claim", "INTEGER DEFAULT 0"),

    ("ai_remark", "TEXT"),

    ("prediction_date", "DATETIME")

]

for column_name, column_type in new_columns:

    if column_name not in columns:

        print(f"Adding column: {column_name}")

        cursor.execute(
            f"ALTER TABLE claims ADD COLUMN {column_name} {column_type}"
        )

connection.commit()

connection.close()

print()

print("=" * 50)
print("Claims table updated successfully.")
print("=" * 50)