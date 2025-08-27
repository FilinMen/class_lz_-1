from pol import Frame

if __name__ == "__main__":
    input_file = r"E:\praktika\class_lz_-1\class_lz_-1\lz_4\var9.csv"
    processor = Frame(input_file)
    removed = ~processor
    processor.split_and_save('Cash-back', 'cashback_true.csv', 'cashback_false.csv')