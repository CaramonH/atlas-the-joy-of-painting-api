import psycopg2
import csv
from datetime import datetime

# Connect to the PostgreSQL database
conn = psycopg2.connect("dbname=joy_of_painting user=postgres host=localhost")
cur = conn.cursor()

# Import data from Colors_Used.csv
with open('Colors_Used.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            "INSERT INTO colors (name, hex_code) VALUES (%s, %s)",
            (row['colors'], row['color_hex'])
        )

# Import data from Episode_Dates.csv
with open('Episode_Dates.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date_str = row['Episode_Dates']
        date_obj = datetime.strptime(date_str, '"%B %d, %Y"')
        cur.execute(
            "INSERT INTO episodes (original_airdate) VALUES (%s)",
            (date_obj.date(),)
        )

# Import data from Subject_Matter.csv
with open('Subject_Matter.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Assuming you have a table called 'subjects' with a column 'name'
        for column, value in row.items():
            if value == '1' and column != 'EPISODE' and column != 'TITLE':
                cur.execute(
                    "INSERT INTO subjects (name) VALUES (%s)",
                    (column,)
                )

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
