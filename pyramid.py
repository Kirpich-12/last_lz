# Finding the volume of a truncated pyramid
#==========================================


# Import libs
from math import sqrt #import module sqrt

# lamda func
Value = lambda s1, s2, h: (h / 3) * (s1 + s2 + sqrt(s1 * s2)) #find value


# Main func
def main():
    s1 = float(input("Введите площадь нижнего основания: "))
    s2 = float(input("Введите площадь верхнего основания: "))
    h = float(input("Введите высоту усечённой пирамиды: "))
    print(f"ОбЪём усечённой пирамиды составляет: {Value(s1, s2, h)}")

if __name__ == "__main__":
    main()