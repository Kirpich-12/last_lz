#Returns the object is floating(Yes/No)
#=====================================


# Finding function
def arch(m:float, V:float, po:float) -> str:
    if po > 1000:
        print("Предмет не плавает")
    elif po == 1000:
        print("Предмет вроде плавает")
    else:
        print("Предмет плавает")


# Main function
def main():
    mass = float(input("Введите массу: "))
    v = float(input("Введите объём погружённой части: "))
    plt = float(input("Введите плотность: "))
    arch(mass, v, plt)

if __name__ == "__main__":
    main()