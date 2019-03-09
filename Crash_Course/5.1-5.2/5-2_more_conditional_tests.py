#!/user/bin/env python3

car_brands = []
car_brands.append('acura')
car_brands.append('honda')
car_brands.append('lexus')
car_brands.append('volkswagon')
car_brands.append('lotus')
car_brands.append('lamboghini')
car_brands.append('mclaren')
car_brands.append('veyron')
car_brands.append('audi')
car_brands.append('bmw')
car_brands.append('formula 1')

cars = []

for name in car_brands:
    if name.lower() == 'mclaren':
        cars.append('McLaren')
    if name.lower() == 'bmw':
        cars.append(name.upper())
    else:
        cars.append(name.title())

cars.sort()
cars.remove('McLaren')

honda = 'acura'
acura = 'honda'

audi = 'volkswagon'
volkswagon = 'audi'

bmw = 'bmw'

print("Is Acura same as Honda?")
print(acura.lower() == 'honda')

print("\nIs BMW same as Audi?")
print(audi.lower() == 'bmw')

john = 22
samantha = 47
kate = 18
kayle = 61
adam = 25

print("\nIs John younger than 11 years old?")
print(john < 11)

print("\nIs Samantha older or equal than 11 years old?")
print(samantha >= 11)

print("\nIs Kate 18 years old?")
print(kate == 18)

print("\nIs Kayle younger or equal than 11 years old?")
print(kayle <= 11)

print("\nIs Adam older than 11 years old?")
print(adam > 11)

print("\nAre Honda and Acura the same company?")
print(acura == 'honda' and honda == 'acura')

print("\nIs BMW or Audi patterned Volkswagon?")
print(bmw == 'volkswagon' or audi == 'volkswagon')

print("\nIs Veyron in my car's list?")
print('Veyron' in cars)

print("\nIs Maserati NOT in my car's list?")
print('Maserati' not in cars)
