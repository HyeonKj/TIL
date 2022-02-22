class Movie:
	def __init__(self, name, teen_price, adult_price):
		self.name = name
		self.teen_price = teen_price
		self.adult_price = adult_price

	def get_name(self):
		return self.name

	def get_teen_price(self):
		return self.teen_price

	def get_adult_price(self):
		return self.adult_price

class Screen:
	def __init__(self, name, seating_arrangement):
		self.name = name
		self.seating_arrangement = seating_arrangement
		self.total_seats_number = 0
		self.set_screen()
		self.reamain_seats_number = self.total_seats_number

	def set_screen(self):
		result = 0
		for cols in self.seating_arrangement:
			for cell in cols:
				if cell == 0:
					result = result + 1
		self.total_seats_number = result

	def get_name(self):
		return self.name

	def set_seating_arrangement(self, seating_arrangement):
		self.seating_arrangement = seating_arrangement

	def get_seating_arrangement(self):
		return self.seating_arrangement

	def show_seating_arrangement(self):
		print(self.seating_arrangement[0])
		print(self.seating_arrangement[1])
		print(self.seating_arrangement[2])
		print(self.seating_arrangement[3])
		print(self.seating_arrangement[4])

class Showing_Infomation:
	def __init__(self, time_slot, movie, screen):
		self.time_slot = time_slot
		self.movie = movie
		self.screen = screen

	def get_time_slot(self):
		return self.time_slot

	def get_movie(self):
		return self.movie

	def get_screen(self):
		return self.screen
def reserve_movie():
	choice = ""
	adult_number = 0
	teen_number = 0
	ticket_price = 0
	coupon = ""
	coupon_price = ""
	payment_price = 0
	seats = []
	global total_gross

	print("--------------------")
	print("상영중인 영화:")
	for movie in movies:
		print(movie)
	print("--------------------")

	# 영화 선택
	movie_choice = input("영화 선택: ")
	while movie_choice not in movies:
		print("다시 입력해주세요.")
		movie_choice = input("영화 선택: ")
# 인원 수 선택
	print("--------------------")
	print("관람객 인원 선택")
	teen_number = input("청소년 수: ")
	while teen_number.isdigit() == False:
		print("다시 입력해주세요.")
		teen_number = input("청소년 수: ")
	teen_number = int(teen_number)
	ticket_price = ticket_price + movies[movie_choice].get_teen_price() * teen_number

	adult_number = input("성인 수: ")
	while adult_number.isdigit() == False:
		print("다시 입력해주세요.")
		adult_number = input("성인 수: ")
	adult_number = int(adult_number)
	ticket_price = ticket_price + movies[movie_choice].get_adult_price() * adult_number

# 쿠폰 여부
	print("--------------------")
	coupon = input("쿠폰을 가지고 계십니까?(y/n): ")
	coupon_price = 0
	while coupon != "y" and coupon != "n":
		print("다시 입력해주세요")
		coupon = input("쿠폰을 가지고 계십니까?(y/n): ")

	# 쿠폰 금액 입력
	if coupon == "y":
		coupon_price = input("할인권의 금액 입력: ")
		while coupon_price.isdigit() == False:
			print("다시 입력해주세요.")
			coupon_price = input("할인권의 금액 입력: ")
		coupon_price = int(coupon_price)

movie1 = Movie("다크나이트", 7000, 10000)
movie2 = Movie("라라랜드", 8000, 10000)
movie3 = Movie("매트릭스", 9000, 11000)
movie4 = Movie("해리포터", 9000, 10000)
movie5 = Movie("기생충", 9000,  11000)
movies = {
	movie1.get_name():movie1, 
	movie2.get_name():movie2, 
	movie3.get_name():movie3,
        movie4.get_name():movie4,
        movie5.get_name():movie5
}

screen1 = Screen("1관", [[0] * 5 for i in range(5)])
screen2 = Screen("2관", [[0] * 5 for i in range(5)])
screen3 = Screen("3관", [[0] * 5 for i in range(5)])
screens = {
	screen1.get_name():screen1,
	screen2.get_name():screen2,
	screen3.get_name():screen3		
}

timetable = {
	movie1.get_name():
	[
		Showing_Infomation("18:00", movie1, screen1),
		Showing_Infomation("23:00", movie1, screen1),
		Showing_Infomation("19:00", movie1, screen2),
		Showing_Infomation("21:40", movie1, screen2)
	],
	movie2.get_name():
	[
		Showing_Infomation("13:00", movie2, screen1),
		Showing_Infomation("15:00", movie2, screen1),
		Showing_Infomation("10:00", movie2, screen2),
		Showing_Infomation("12:40", movie2, screen2)
	],
	movie3.get_name():
	[
		Showing_Infomation("10:30", movie3, screen3),
		Showing_Infomation("12:50", movie3, screen3),
		Showing_Infomation("15:10", movie3, screen3),
		Showing_Infomation("17:30", movie3, screen3),
		Showing_Infomation("19:50", movie3, screen3)
	],
        movie4.get_name():
        [
                Showing_Infomation("10:30", movie3, screen3),
		Showing_Infomation("12:50", movie3, screen3),
		Showing_Infomation("15:10", movie3, screen3),
		Showing_Infomation("17:30", movie3, screen3),
		Showing_Infomation("19:50", movie3, screen3)
        ],
        movie5.get_name():
        [
                Showing_Infomation("10:30", movie3, screen3),
		Showing_Infomation("12:50", movie3, screen3),
		Showing_Infomation("15:10", movie3, screen3),
		Showing_Infomation("17:30", movie3, screen3),
		Showing_Infomation("19:50", movie3, screen3)
	]
}

total_gross = 0
is_run = True

while(is_run):
	command = input("1.영화 예매 2.영화 시간표 확인 3.총매출 확인 4.프로그램 종료: ")
	if command == "1":
		reserve_movie()
	elif command == "2":
		confirm_movie_timetable()
	elif command == "3":
		show_total_gross()
	elif command == "4":
		exit()
	else:
		print("다시 입력해주세요.")
		

