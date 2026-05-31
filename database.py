import sqlite3

def init_db(db_path, txt_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS words (word TEXT PRIMARY KEY)")
    with open(txt_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
        cursor.executemany("INSERT OR IGNORE INTO words VALUES (?)", [(w,) for w in words])
    conn.commit()
    conn.close()

def check_word_exists(db_path, word):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def get_all_words_from_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM words")
    words = [row[0] for row in cursor.fetchall()]
    conn.close()
    return words
