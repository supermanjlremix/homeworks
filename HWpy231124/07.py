questions = [
    "1. Какая столица Франции?\n   a) Лондон\n   b) Париж\n   c) Рим\n",
    "2. Какое самое высокое здание в мире?\n   a) Эмпайр-стейт-билдинг\n   b) Бурдж-Халифа\n   c) Шанхайская башня\n",
    "3. Какая самая длинная река в мире?\n   a) Амазонка\n   b) Нил\n   c) Янцзы\n"
]

correct_answers = ['b', 'b', 'a']
score = 0
for i in range(len(questions)):
    answer = input(questions[i]).lower()  
    if answer == correct_answers[i]:
        score += 2

print("Вы набрали", score, "балл(ов).")
