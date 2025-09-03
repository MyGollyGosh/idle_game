import sqlite3
from datetime import datetime
from lib.generate_text import generate_output

def insert_story(timestamp):
    """
    Insert a story with current timestamp into the stories database.
    
    Args:
        generate_story (str): The story content to insert
    """
    # Connect to the SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('stories.db')
    cursor = conn.cursor()
    
    # Create the stories table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            story_text TEXT NOT NULL
        )
    ''')
    
    # Get current timestamp
    current_timestamp = datetime.now()
    
    # Insert the story with timestamp
    cursor.execute('''
        INSERT INTO stories (timestamp, story_text)
        VALUES (?, ?)
    ''', (current_timestamp, generate_output(timestamp)))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print(f"Story inserted successfully at {current_timestamp}")