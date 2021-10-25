import random
import sqlite3

connection = sqlite3.connect('potterrina.sqlite')
cursor = connection.cursor()


class Player:
	def __init__(self, name, total1 = 0):
		self.name = name
		self.total = total1
		print("Добро пожаловать в нашу игру на каверзные вопросы по вселенной Поттерианы! Да начнется первый раунд! P.S. Чтобы выйти из игры введите: 0")

name = input('Ваше имя: ')
player_1 = Player(name)

def format(level):
    # level = 1
    cursor.execute('SELECT COUNT(*) FROM round_%d' % level)
    fa = cursor.fetchall()
    d = random.randint(1, fa[0][0])
    cursor.execute('SELECT question FROM round_%d WHERE id=%d;' % (level, d))
    # cursor.execute('SELECT question FROM round_1 WHERE id=' + str(d) +';')
    row = (cursor.fetchall())
    print(row[0][0])
    cursor.execute('SELECT ans_1, ans_2, ans_3, ans_4 FROM round_%d WHERE id=%d;' % (level, d))
    answers = (cursor.fetchall())[0]
    [print(i + 1, ':', answer) for i, answer in zip(range(len(answers)), answers)]
    cursor.execute('SELECT question, ans_1, ans_2, ans_3, ans_4, right_ans FROM round_%d WHERE id=%d;' % (level, d))
    list_ = (cursor.fetchall())
    q, a1, a2, a3, a4, ra = list_[0]
    # print(list_)
    
    try:
        a_r = int(input())
    except Exception as err:
        print("""
        Сломал? Почини.
        """, err)
        quit()
        
    if a_r == 1:
        a_r = a1
    if a_r == 2:
        a_r = a2
    if a_r == 3:
        a_r = a3
    if a_r == 4:
        a_r = a4
    if a_r == ra:
        print("""
        Поттерманам привет! Следующий вопрос... 
        """)
        level += 1
    else:
        print("""
        Неудача :( 
        """)
        quit()

    return level

level = 1
while level < 6:
    level = format(level)
else:
    print("Я устала кодить :(")
    
connection.commit()
cursor.close()
connection.close()
