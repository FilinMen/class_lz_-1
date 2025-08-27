from zivotnoe import Creauters, Tiger

def main():
    input_data = input('Введите кличку, возраст, вид, породу, статус охранника: ')
    data = input_data.split()

    name = str(data[0])
    age = int(data[1])
    species = str(data[2])
    breed = str(data[3])
    guard_status = str(data[4])

    print("Information about Creauters:")
    animal = Creauters(name, age, species)
    animal.info()

    print("Information about Tiger:")
    tiger = Tiger(name, age, species, breed, guard_status)
    tiger.info()
    tiger.guard_house()

if __name__ == "__main__":
    main()