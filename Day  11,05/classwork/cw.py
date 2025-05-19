# 3)ჩაწერე განსხვავებული მონაცემთა ტიპების (int, float, string, boolean) ცვლადები
name ="giorgi"
age = 11
num1 = 10.5
num = True and False

print(name, age, num, num1)

# 4)მომხმარებელს შემოატანინეთ მისი ასაკი და type() ფუნქციით შეამოწმეთ,თუ რა ტიპის მონაცემია შემოტანილი ასაკი.

age = 18
print(type(age))

# 5)მომხმარებელს შემოატანინე მისი ასაკი და ბოლოს დაბეჭდე თუ რამდენი წლის იქნება ის 5 წლის შემდეგ

age = int(input("Enter your age: "))
print(age + int(5))

# 6)მომხმარებელს შემოატანინეთ სახელი გვარი ასაკი სიმაღლე საყვარელი ფერი და გამოიტანეთ ეს ყველაფერი ერთ დიდ წინადადებაში.

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
favorite_color = input("Enter your favorite color: ")
print(name, + surname, + int(age) + float(height) + favorite_color)



