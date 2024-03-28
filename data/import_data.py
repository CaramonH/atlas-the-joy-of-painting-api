import psycopg2
from datetime import datetime

# Connect to the PostgreSQL database
conn = psycopg2.connect("dbname=joy_of_painting user=postgres password=2016 host=localhost")
cur = conn.cursor()

# Function to insert data into the episodes table
def insert_episode(title, airdate):
    cur.execute("INSERT INTO episodes (title, original_airdate) VALUES (%s, %s)", (title, airdate))
    conn.commit()
    print(f"Inserted episode: title={title}, airdate={airdate}")

# Function to insert data into the colors table
def insert_color(color_data):
    parts = color_data.split(',')
    color_id = parts[0].strip()
    colors_list = parts[8].strip(']["').split("', '")
    for color in colors_list:
        cur.execute("INSERT INTO colors (color_id, name) VALUES (%s, %s)", (color_id, color))
        conn.commit()
        print(f"Inserted color: id={color_id}, name={color}")

# Read data from Colors_Used.txt and insert into colors table
with open('Colors_Used', 'r') as f:
    next(f)  # Skip the header row
    for line in f:
        insert_color(line)

# Function to insert data into the subjects table
def insert_subject(subject_id, name):
    cur.execute("INSERT INTO subjects (id, name) VALUES (%s, %s)", (subject_id, name))
    conn.commit()
    print(f"Inserted subject: id={subject_id}, name={name}")

# Function to parse date string into a valid date format
def parse_date(date_str):
    try:
        return datetime.strptime(date_str.split(')')[0], '%B %d, %Y').date()
    except ValueError:
        return None

# Read data from Episode_Dates.txt and insert into episodes table
with open('Episode_Dates', 'r') as f:
    for line in f:
        parts = line.strip().split('" (')
        title = parts[0].strip('"')
        airdate = parse_date(parts[1].strip(')').strip('"'))
        insert_episode(title, airdate)

# Read data from Colors_Used.txt and insert into colors table
with open('Colors_Used', 'r') as f:
    next(f)  # Skip the header row
    for line in f:
        parts = line.strip().split(',')
        color_id, name = parts
        insert_color(color_id.strip(), name.strip())

# Read data from Subject_Matter.txt and insert into subjects table
with open('Subject_Matter', 'r') as f:
    next(f)  # Skip the header row
    for line in f:
        parts = line.strip().split(',')
        subject_id = parts[0].strip('"')
        subject_name = parts[1].strip('"')
        insert_subject(subject_id, subject_name)

# Close the cursor and connection
cur.close()
conn.close()
