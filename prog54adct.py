car1 = {
  "miles": 286,
  "gallons": 9
}

car2 = {
  "miles": 412,
  "gallons": 40
}

car3 = {
  "miles": 361,
  "gallons": 18
}

car4 = {
  "miles": 161,
  "gallons": 11
}

car = {
  "1970VW Bug": car1,
  "1979 Firebird": car2,
  "1980 Subaru": car3,
  "1975 Cutlass": car4
}

print("choose a car from the following", car.keys())
mycar = input()

carselected = car[mycar]
miles = carselected["miles"]
gallons = carselected["gallons"]
mpg = float(miles) / gallons

print("Miles:", miles)
print("gallons:", gallons)
print("MPG:", round(mpg, 10))