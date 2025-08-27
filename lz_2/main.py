from animka import Animal, Dog

def main():
    input_data = input('Введите кличку, возраст, вид, породу, статус охранника: ')
    data = input_data.split()

    name = str(data[0])
    age = int(data[1])
    species = str(data[2])
    breed = str(data[3])
    guard_status = str(data[4])

    print("Инфа об Animal:")
    animal = Animal(name, age, species)
    animal.info()

    print("Инфа о Dog:")
    dog = Dog(name, age, species, breed, guard_status)
    dog.info()
    dog.guard_house()

if __name__ == "__main__":
    main()