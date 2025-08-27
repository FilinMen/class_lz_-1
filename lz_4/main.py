from polymorf import Money

if __name__ == "__main__":
    input_file = r"C:\Users\Asus\Desktop\new practic\class_lz_-1\lz_4\var10.csv"
    processor = Money(input_file)
    removed = ~processor
    processor.split_and_save('Сумма cash-back', 'Сумма cash-back_true.csv', 'Сумма cash-back_false.csv')