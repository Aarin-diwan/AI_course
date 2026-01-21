# Main Menu
while True:
    print("\n🍫 Main Menu")
    print("1. Milk Chocolates")
    print("2. Dark Chocolates")
    print("3. White Chocolates")
    print("4. Chocolate Bars")
    print("5. Chocolate Gifts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Milk Chocolates
    if choice == 1:
        print("\nMilk Chocolates")
        print("1. Dairy Milk")
        print("2. 5 Star")
        print("3. KitKat")
        print("4. Munch")
        print("5. Perk")
        print("6. Back")
        sub = int(input("Select option: "))
        if sub == 6:
            continue
        else:
            print("Milk Chocolate selected")

    # 2. Dark Chocolates
    elif choice == 2:
        print("\nDark Chocolates")
        print("1. Bournville")
        print("2. Amul Dark")
        print("3. Lindt Dark")
        print("4. Hershey Dark")
        print("5. Cadbury Dark")
        print("6. Back")
        sub = int(input("Select option: "))
        if sub == 6:
            continue
        else:
            print("Dark Chocolate selected")

    # 3. White Chocolates
    elif choice == 3:
        print("\nWhite Chocolates")
        print("1. Milkybar")
        print("2. KitKat White")
        print("3. Galaxy White")
        print("4. Toblerone White")
        print("5. Lindt White")
        print("6. Back")
        sub = int(input("Select option: "))
        if sub == 6:
            continue
        else:
            print("White Chocolate selected")

    # 4. Chocolate Bars
    elif choice == 4:
        print("\nChocolate Bars")
        print("1. KitKat")
        print("2. Snickers")
        print("3. Mars")
        print("4. Twix")
        print("5. Bounty")
        print("6. Back")
        sub = int(input("Select option: "))
        if sub == 6:
            continue
        else:
            print("Chocolate Bar selected")

    # 5. Chocolate Gifts
    elif choice == 5:
        print("\nChocolate Gifts")
        print("1. Chocolate Box")
        print("2. Assorted Pack")
        print("3. Festival Gift Pack")
        print("4. Kids Gift Pack")
        print("5. Premium Gift Box")
        print("6. Back")
        sub = int(input("Select option: "))
        if sub == 6:
            continue
        else:
            print("Chocolate Gift selected")

    # Exit
    elif choice == 6:
        print("Thank you 🍫 Visit again!")
        break

    else:
        print("Invalid choice")
      
