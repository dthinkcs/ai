
def main():
    filename = input("Enter filename(default mushrooms.csv): ")
    if filename == "":
        filename = "mushrooms.csv"
    
    file_handler = open(filename)
    for line in file_handler: # yield is useful when file too large to fit in mem (lazy evaluation)

        




if __name__ == "__main__":
    main()