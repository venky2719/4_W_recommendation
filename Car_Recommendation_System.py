import csv
from collections import OrderedDict
import operator
from Car import Car, Maruti, MPV, Hatchback, Pickup, SUV
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

if __name__ == '__main__':
	car_array = []
	images_dir = 'images/'
	print("""Select the type of car you preferred, (-1 to exit):
 1. Maruti
 2. SUV
 3. MPV
 4. Hatchback
 5. Pickup""")
	t = int(input("Your selection: "))
	with open('car_info.csv', newline='') as f:
		reader = csv.reader(f)
		next(reader)
	with open('Spreadsheet.csv', newline='') as f:
		reader = csv.reader(f)
		
		row_num = len(open("Spreadsheet.csv").readlines()) - 1
		if t == 1:
			for i in range(row_num):
				row = next(reader)
				if row[2] == "Maruti":
					car_array.append(Maruti(row))
		elif t == 2:
			for i in range(row_num):
				row = next(reader)
				if row[2] == "SUV":
					car_array.append(SUV(row))
		elif t == 3:
			for i in range(row_num):
				row = next(reader)
				if row[2] == "MPV":
					car_array.append(MPV(row))
		elif t == 4:
			for i in range(row_num):
				row = next(reader)
				if row[2] == "hatchback":
					car_array.append(Hatchback(row))
		elif t == 5:
			for i in range(row_num):
				row = next(reader)
				if row[2] == "pickup":
					car_array.append(Pickup(row))

	for i in range(len(car_array)):
			for j in range(len(car_array) - 1):
				if float(car_array[j].overall_rat) < float(car_array[j + 1].overall_rat):
					temp = car_array[j]
					car_array[j] = car_array[j + 1]
					car_array[j + 1] = temp
	choice = []
	result = OrderedDict()
	while True:
		print("\n1. brand 2. model 3. price 4. engine size 5. fuel type")
		c = input("Select the main criteria which you concern the most: (-1 to exit)\nYour selection: ")
		if int(c) == -1:
			if str(result) == "OrderedDict()":
				for car in car_array:
					result[car.model] = 1
			break
		if c in choice:
			print("Already selected.")
			continue
		elif not c.isdigit() or int(c) > 5 or int(c) < 1:
			print("Enter digits 1 to 5 only.")
			continue
		else:
			choice.append(c)

		if c == "1":
			print("""
Which brand do you prefer? Enter your choice, or "-1" to exit selection:
""")
			check = []
			for car in car_array:
				if car.brand not in check:
					check.append(car.brand)
					print(" " + car.brand)
			c = input("Your choice: ").lower()
			if c == "-1":
				del choice[len(choice) - 1]
				continue
			for car in car_array:
				if car.brand.lower() == c:
					if car.model not in result:
						result[car.model] = 1
					else:
						result[car.model] += 1
		elif c == "2":
			print("""
Which model do you prefer? Enter your choice, or "-1" to exit selection:
""")
			for car in car_array:
				print(" " + car.model)

			c = input("Your choice: ").lower()
			if c == "-1":
				del choice[len(choice) - 1]
				continue
			for car in car_array:
				if car.model.lower() == c:
					if car.model not in result:
						result[car.model] = 1
					else:
						result[car.model] += 1

		elif c == "3":
			print("\nWhat is your maximum afforadable budget? Enter your preference, or \"-1\" to exit selection")
			if c == "-1":
				del choice[len(choice) - 1]
				continue
			c = int(input("Your budget: "))
			for car in car_array:
				if int(car.price) <= c:
					if car.model not in result:
						result[car.model] = 1
					else:
						result[car.model] += 1
		elif c == "4":
			print("\nSelect your prefered engine size range. (1.0 - 3.0), or \"-1\" to exit selection")
			
			low_bound = float(input("Lower boundary: "))
			hi_bound = float(input("Higher boundary: "))
			if low_bound == -1 or hi_bound == -1:
				del choice[len(choice) - 1]
				continue
			for car in car_array:
				if float(car.engineSize) >= low_bound and float(car.engineSize) <= hi_bound:
					if car.model not in result:
						result[car.model] = 1
					else:
						result[car.model] += 1
		elif c == "5":
			print("""
Select your prefered fuel type. Enter your choice, or "-1" to exit selection:
 Petrol
 Hybrid
 Diesel
""")
			c = input("Your choice: ").lower()
			if c == "-1":
				del choice[len(choice) - 1]
				continue
			for car in car_array:
				if car.fuelType.lower() == c:
					if car.model not in result:
						result[car.model] = 1
					else:
						result[car.model] += 1

	sorted_result = []
	for key, value in result.items():
	    temp = [key, value]
	    sorted_result.append(temp)
	sorted_result = Sort(sorted_result)
	
	if not sorted_result:
		print("Sorry, no suggestions found.")
	else:
		print("Result:")
		i = 1
		print("Total of " + str(len(sorted_result)) + " suggestions:")
		for x in sorted_result:
			car_img = x[0] + '.jpg'
			attribute = ""

			for car in car_array:
				if car.model == x[0]:
					attribute = car.print_attributes()
					print("Suggestion " + str(i))
					print(attribute)
					print()
					break

			text = "Suggestion " + str(i) + "-\n" + attribute #x[0].print_attributes()
			img = Image.open(images_dir + car_img)
			img.thumbnail((800, 800))
			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("Bevan.ttf", 16)
			draw.rectangle(((0, 00), (200, 200)), fill="white", outline = "black")
			draw.text((10, 10), text, (0,0,0), font = font)
			img.show()
			i += 1
