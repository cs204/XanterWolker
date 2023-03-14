def main (str, sep=' '):

    SnakeReg = ''
    for i in str:
        if i.isupper():
            SnakeReg = SnakeReg + sep + i.lower()
        else:
            SnakeReg = SnakeReg + i
    print(SnakeReg.lstrip(sep))

CamelReg = input("Верблюжий стиль: ")
main(CamelReg, '_')