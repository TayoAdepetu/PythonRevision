def main():
    # name = get_name()
    # house = get_house()

    name, house = get_student()
    print(f"{name} is from {house}")

# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__=="__main__":
    main()
