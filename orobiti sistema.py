def sistema() :
    number = int(input("same number: "))

    while number != 0 :
        if int(number) % 2 != 0 :
            orobiti_sistema.append(1)
        elif int(number) % 2 == 0 :
            orobiti_sistema.append(0)
        yield int(number)
        number /= 2

number = int(input("number: "))

orobiti_sistema = []

a = sistema()

while int(number) >= 1 :
    print(next(a))
    number /= 2
    
print(f"Binary code: {orobiti_sistema}")