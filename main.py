import os
import sys
# Path ni to'g'rilash
sys.path.append(os.getcwd())

from database import init_db, check_word_exists, get_all_words_from_db
from engine import get_best_match

DB_FILE = "data/dictionary.db"
TXT_FILE = "data/raw_data.txt"

# Ma'lumotlar bazasini tayyorlash
if not os.path.exists("data"):
    os.makedirs("data")

# Baza yaratish (agar yo'q bo'lsa)
init_db(DB_FILE, TXT_FILE)

# Asosiy logika
word = input("So'zni kiriting: ").strip().lower()

if check_word_exists(DB_FILE, word):
    print("To'g'ri ✅")
else:
    all_words = get_all_words_from_db(DB_FILE)
    suggestion = get_best_match(word, all_words)
    if suggestion:
        print(f"Xato! Balki buni nazarda tutgandirsiz: {suggestion} ✅")
    else:
        print("Xato! Tavsiya topilmadi ❌")
