try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income / age
    print("Your age is", age)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter an integer")

