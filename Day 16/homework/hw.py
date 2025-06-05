# 1)მომხმარებელს შემოატანინეთ რაღაც რიცხვი და შემდეგ შეამოწმეთ თუ ეს რიცხვი არის ლუწი,დაბეჭდეთ "even", ხოლო თუ კენტია "odd"

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
    