import csv
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="joy_of_painting",
        user="postgres",
        password="2016",
        host="localhost",
    )

def insert_episode(conn, episode_id, title, season, episode, colors, subjects, air_date, month, notes, image_src, youtube_src):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO episodes (episode_id, title, season, episode, colors, subjects, air_date, month, notes, image_src, youtube_src) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (episode_id, title, season, episode, colors, subjects, air_date, month, notes, image_src, youtube_src)
        )

def insert_color(conn, color_id, color_name):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO colors (color_id, color_name) VALUES (%s, %s)",
            (color_id, color_name)
        )

def insert_subject(conn, subject_id, subject_name):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO subjects (subject_id, subject_name) VALUES (%s, %s)",
            (subject_id, subject_name)
        )

def main():
    conn = get_connection()

    # Initialize lists to store data
    titles = []
    seasons = []
    episodes = []
    ep_colors = []
    air_dates = []
    months = []
    notes = []
    image_srcs = []
    youtube_srcs = []
    colors_used = []
    subjects_used = []
    all_colors = []
    all_subjects = []

    # Open and process Episode_Dates file
    with open('Episode_Dates', 'r') as file:
        for line in file:
            line = line.strip()
            start_index = line.find('(')
            end_index = line.find(')')
            
            if start_index != -1 and end_index != -1:
                date_str = line[start_index + 1:end_index]
                notes_start_index = end_index + 1
                if notes_start_index < len(line):
                    note = line[notes_start_index:].strip()
                else:
                    note = ''
                
                air_dates.append(date_str)
                month = date_str.split()[0]
                months.append(month)
                notes.append(note)

    # Open and process Subject_Matter file
    with open('Subject_Matter', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        all_subjects = header_row[2:67]
        all_subjects = [phrase.lower().replace('_', ' ').title() for phrase in all_subjects]
        for row in reader:
            current_subjects = []
            if len(row) <= 69:
                for i in range(2, 69):
                    if row[i].strip() == '1':
                        current_subjects.append(i - 1)
            subjects_used.append(','.join(map(str, current_subjects)))

    # Open and process Colors_Used file
    with open('Colors_Used', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        all_colors = header_row[10:28]
        all_colors = [phrase.lower().replace('_', ' ').title() for phrase in all_colors]
        for row in reader:
            current_colors = []
            if len(row) <= 28:
                for i in range(10, 28):
                    if row[i].strip() == '1':
                        current_colors.append(i - 9)
            info = row
            title = row[3]
            season = row[4]
            episode = row[5]
            colors = row[8]
            image_src = row[2]
            youtube_src = row[7]
            color_data = eval(colors)
            csv_color_string = ','.join(color_data)
            list_data_cleaned = csv_color_string.replace('\r', '').replace('\n', '')

            titles.append(title)
            seasons.append(season)
            episodes.append(episode)
            ep_colors.append(list_data_cleaned)
            colors_used.append(','.join(map(str, current_colors)))
            image_srcs.append(image_src)
            youtube_srcs.append(youtube_src)

    for i in range(len(titles)):
        insert_episode(conn, i + 1, titles[i], seasons[i], episodes[i], colors_used[i], subjects_used[i], air_dates[i], months[i], notes[i], image_srcs[i], youtube_srcs[i])

    for i in range(len(all_colors)):
        insert_color(conn, i + 1, all_colors[i])

    for i in range(len(all_subjects)):
        insert_subject(conn, i + 1, all_subjects[i])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()