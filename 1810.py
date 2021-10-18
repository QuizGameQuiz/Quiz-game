class Player:
	def __init__(self, name, total1 = 0):
		self.name = name
		self.total = total1
		print("Добро пожаловать в нашу игру на каверзные вопросы по вселенной Поттерианы! Да начнется первый раунд! P.S. Чтобы выйти из игры введите: 0")
		
	def incr(self):
		self.total += 1
		
	def decr(self):
		self.total -= 1
	
	def round_1(self):
		if self.total >= 0:
			print("Поздравляем! Вы прошли во 2-й раунд! Ваш счёт: {}".format(self.total))
			self.total = 0
		else:
			print("К сожалению, вы не прошли 1-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие!")
			exit()
	def round_2(self):
		if self.total >= 0:
			print("Поздравляем! Вы прошли в 3-й раунд! Ваш счёт: {}".format(self.total))
			self.total = 0
		else:
			print("К сожалению, вы не прошли 2-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы все равно молодец!")
			exit()
	def round_3(self):
		if self.total >= 0:
			print("Поздравляем! Вы прошли в 4-й раунд! Ваш счёт: {}".format(self.total))
			self.total = 0
		else:
			print("К сожалению, вы не прошли 3-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы прекрасны!")
			exit()
	def round_4(self):
		if self.total >= 0:
			print("Поздравляем! Вы прошли в 5-й раунд! Ваш счёт: {}".format(self.total))
			self.total = 0
		else:
			print("К сожалению, вы не прошли 4-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы бьютифул!")
			exit()
	def round_5(self):
		if self.total >= 0:
			print("Поздравляем! Вы победили!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли финальный раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы просто монстр!")
			exit()

name = input('Ваше имя: ')
player_1 = Player(name)

round_1_questions = {"Как звали сову Гарри Поттера?": ['1. Кукля ' '2. Букля ' '3. Бублик ' '4. Хадвиг'], "Какой герой был оборотнем?": ['1. Сириус Блэк ' '2. Том Реддл ' '3. Римус Люпин ' '4. Драко Малфой']}
round_1_answers = {"Как звали сову Гарри Поттера?": 2, "Какой герой был оборотнем?": 3}

count = 0
lifeline = True

for question in round_1_questions:
	if count < 2:
		print("Вопрос: ")
		print(question)
		print(round_1_questions[question])
		answer = input("Ответ: ")
		if int(answer) == round_1_answers[question]:
			player_1.incr()
			print('Поздравляем с правильным ответом!')
			count += 1
		elif answer == '0':
			print("Вы решили выйти из игры :(")
			exit()
		else:
			print("К сожалению, вы ошиблись :(")
			player_1.decr()
			count -= 1 and lifeline == False
player_1.round_1()

round_2_questions = {"Кто бросил имя Гарри Поттера в кубок огня?": ['1. Грюм ' '2. Дамблдор ' '3. Сам Гарри ' '4. Крауч'], "На какой позиции играл Рон Уизли в квиддиче?": ['1. Защита ' '2. Охотник ' '3. Не играл в квиддич ' '4. Вратарь']}
round_2_answers = {"Кто бросил имя Гарри Поттера в кубок огня?": 4, "На какой позиции играл Рон Уизли в квиддиче?": 4}

count = 0
lifeline = True

for question in round_2_questions:
	if count < 2:
		print("Вопрос: ")
		print(question)
		print(round_2_questions[question])
		answer = input("Ответ: ")
		if int(answer) == round_2_answers[question]:
			player_1.incr()
			print('Поздравляем с правильным ответом!')
			count += 1
		elif answer == '0':
			print("Вы решили выйти из игры :(")
			exit()
		else:
			print("К сожалению, вы ошиблись :(")
			player_1.decr()
			count -= 1 and lifeline == False
player_1.round_2()

round_3_questions = {"Кем приходился Драко Малфой Андромеде Тонкс?": ['1. Кузен ' '2. Племянник ' '3. Младший брат ' '4. Сын'], "Сколько раз Гарри Поттер использовал Непростительные заклинания?": ['1. Ни разу ' '2. 3 раза ' '3. 5 раз ' '4. 6 раз']}
round_3_answers = {"Кем приходился Драко Малфой Андромеде Тонкс?": 2, "Сколько раз Гарри Поттер использовал Непростительные заклинания?": 4}

count = 0
lifeline = True

for question in round_3_questions:
	if count < 2:
		print("Вопрос: ")
		print(question)
		print(round_3_questions[question])
		answer = input("Ответ: ")
		if int(answer) == round_3_answers[question]:
			player_1.incr()
			print('Поздравляем с правильным ответом!')
			count += 1
		elif answer == '0':
			print("Вы решили выйти из игры :(")
			exit()
		else:
			print("К сожалению, вы ошиблись :(")
			player_1.decr()
			count -= 1 and lifeline == False
player_1.round_3()

round_4_questions = {"Что преподавал профессор Дамблдор, пока не получил должность директора?": ['1. Защита от тёмных искусств ' '2. Древние руны ' '3. Трансфигурацию ' '4. Защиту от светлых искусств'], "Кто из семьи Уизли погиб во время битвы за Хогвартс?": ['1. Джордж Уизли ' '2. Чарли Уизли ' '3. Фред Уизли ' '4. Джинни Уизли']}
round_4_answers = {"Что преподавал профессор Дамблдор, пока не получил должность директора?": 3, "Кто из семьи Уизли погиб во время битвы за Хогвартс?": 3}

count = 0
lifeline = True

for question in round_4_questions:
	if count < 2:
		print("Вопрос: ")
		print(question)
		print(round_4_questions[question])
		answer = input("Ответ: ")
		if int(answer) == round_4_answers[question]:
			player_1.incr()
			print('Поздравляем с правильным ответом!')
			count += 1
		elif answer == '0':
			print("Вы решили выйти из игры :(")
			exit()
		else:
			print("К сожалению, вы ошиблись :(")
			player_1.decr()
			count -= 1 and lifeline == False
player_1.round_4()

round_5_questions = {"В каком возрасте дети получают письмо из хогвартса?": ['1. 12 ' '2. 11 ' '3. 14 ' '4. 10 '], "Из чего сделана палочка Гарри Поттера?": ['1. Жила дракона ' '2. Перо феникса ' '3. Остролист ' '4. Береза ']}
round_5_answers = {"В каком возрасте дети получают письмо из хогвартса?": 4, "Из чего сделана палочка Гарри Поттера?": 4}

count = 0
lifeline = True

for question in round_5_questions:
	if count < 2:
		print("Вопрос: ")
		print(question)
		print(round_5_questions[question])
		answer = input("Ответ: ")
		if int(answer) == round_5_answers[question]:
			player_1.incr()
			print('Поздравляем с правильным ответом!')
			count += 1
		elif answer == '0':
			print("Вы решили выйти из игры :(")
			exit()
		else:
			print("К сожалению, вы ошиблись :(")
			player_1.decr()
			count -= 1 and lifeline == False
player_1.round_5()
