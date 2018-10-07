import json

datos = open("cars.json")
cars = datos.read()
datos.close()

cars = json.loads(cars)

matricula = ""
mediaMax = 0

for x in range(len(cars['cars'])):
    years = 2018 - cars['cars'][x]['year']
    media = cars['cars'][x]['km'] // years
    if mediaMax < media:
        mediaMax = media
        matricula = cars['cars'][x]['licenseplate']

print(matricula)
