from rapidfuzz import process

def get_best_match(word, db_words):
    # Eng yaqin o'xshash so'zni topish (score 80 dan yuqori bo'lsa)
    match = process.extractOne(word, db_words)
    if match and match[1] > 70:  # 70% o'xshashlik chegarasi
        return match[0]
    return None
