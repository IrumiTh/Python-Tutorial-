def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')
    print("welcome!")


print("Start")
greet_user(last_name="Smith", first_name="John")
#we can add keyword argument after the positional argument
greet_user("Mosh", last_name="Hemin")
print("Finish")
