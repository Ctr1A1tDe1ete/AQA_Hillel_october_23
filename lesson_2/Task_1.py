age = int(input("how old are you?"))

if age <= 7:
    print("Де твої батьки?")
else:
    if age < 16:
        print("Це фільм для дорослих!")
    else:
        if age <= 65:
            print("Ви можете придбати квіток!")
        else:
            print("Покажіть пенсійне посвідчення!")



