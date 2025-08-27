import animals as p

def main():
    print('')


if __name__ == "__main__":
    animal = p.Animal("Барсик", 3, "Кошка")
    animal.make_sound()
    animal.info()
    print()

    dog = p.Dog("Рекс", 5, "Собака", "Овчарка")
    dog.make_sound()
    dog.info()
    print()