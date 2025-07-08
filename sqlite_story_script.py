import sqlite3
from datetime import datetime
from lib.generate_text import generate_output

def insert_story():
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
    ''', (current_timestamp, generate_output(' ')))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print(f"Story inserted successfully at {current_timestamp}")

# Example usage
if __name__ == "__main__":
    # Your story content variable
    generate_story = "Once upon a time, in a land far away, there lived a brave knight who embarked on an epic quest to save the kingdom from an ancient curse."
    
    # Insert the story
    insert_story()
    
    # Optional: View all stories in the database
    def view_all_stories():
        conn = sqlite3.connect('stories.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, timestamp, story_text FROM stories ORDER BY timestamp DESC')
        stories = cursor.fetchall()
        
        print("\nAll stories in database:")
        print("-" * 50)
        for story_id, timestamp, text in stories:
            print(f"ID: {story_id}")
            print(f"Timestamp: {timestamp}")
            print(f"Story: {text[:100]}{'...' if len(text) > 100 else ''}")
            print("-" * 50)
        
        conn.close()
    
    # Uncomment to view all stories
    # view_all_stories()