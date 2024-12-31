#Returns the object is floating(Yes/No)
#=====================================


# Finding function
def arch(m, V, po):
    if po > 1:
        print("Предмет не плавает")
    elif po == 1:
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