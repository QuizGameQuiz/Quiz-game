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
		if self.total >= 1:
			print("Поздравляем! Вы прошли во 2-й раунд!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли 1-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие!")
			exit()
	def round_2(self):
		if self.total >= 1:
			print("Поздравляем! Вы прошли в 3-й раунд!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли 2-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы все равно молодец!")
			exit()
	def round_3(self):
		if self.total >= 1:
			print("Поздравляем! Вы прошли в 4-й раунд!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли 3-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы прекрасны!")
			exit()
	def round_4(self):
		if self.total >= 2:
			print("Поздравляем! Вы прошли в 5-й раунд!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли 4-й раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы бьютифул!")
			exit()
	def round_5(self):
		if self.total >= 1:
			print("Поздравляем! Вы победили!")
			self.total = 0
		else:
			print("К сожалению, вы не прошли финальный раунд. Ваш счёт: {}".format(self.total))
			print("Спасибо за участие! Вы просто монстр!")
			exit()

name = input('Ваше имя: ')
player_1 = Player(name)

round_1_questions = {"Как звали сову Гарри Поттера?": ['1. Кукля ' '2. Букля ' '3. Бублик ' '4. Хадвиг '], "Какой герой был оборотнем?": ['1. Сириус Блэк ' '2.Том Реддл ' '3. Римус Люпин ' '4. Драко Малфой ']}
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

round_2_questions = {"Кто бросил имя Гарри Поттера в кубок огня?": ['1. Грюм ' '2. Дамблдор ' '3. Сам Гарри ' '4. Крауч '], "На какой позиции играл Рон Уизли в квиддиче?": ['1. Защита ' '2. Охотник ' '3. Не играл в квиддич ' '4. Вратарь ']}
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
