import math

def printIntro():
    print("Bu basit bir hesap makinesidir.")
print("Isleminizi secin:\n1) Toplama\n2) Cikarma\n3) Bolme\n4) Carpma")

while True:
    operator = input("Tercihiniz nedir? (+ - / *): \n")

    if operator in('+', '-', '/', '*'):
        #kullanıcı sonlandırana kadar numaraları listeye ekleme
        #listeyi kullanıcı eklemelerine göre güncelleme

        list = []
        num = float(input("Islem yapmak istediginiz sayi miktari nedir?: "))
        for n in range(num):
            numbers = float(input("Islem yapmak istediginiz sayilar nelerdir?: "))
        list.append(numbers)
        if n == '':
            break

        if operator == '+':
            print(add(list))

        if operator == '-':
            print(subtract(list))

        if operator == '/':
            print(divide(list))

        if operator == '*':
            print(multiply(list))
    else:
        break
