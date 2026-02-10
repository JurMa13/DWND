while True:
    # Main Menu
    print("\n========== MAIN MENU ==========")
    print("1. New Game")
    print("2. Quit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        # Character Selection Menu
        while True:
            print("\n===== CHARACTER SELECTION =====")
            print("1. Paladin")
            print("2. Warrior")
            print("3. Archer")
            print("4. Mage")
            print("5. Back")
            
            character_choice = input("Choose your character (1-5): ")
            
            if character_choice == "1":
                print("\nStarting game as Paladin!")
                # Your game code would go here
                break
            
            elif character_choice == "2":
                print("\nStarting game as Warrior!")
                # Your game code would go here
                break
            
            elif character_choice == "3":
                print("\nStarting game as Archer!")
                # Your game code would go here
                break
            
            elif character_choice == "4":
                print("\nStarting game as Mage!")
                # Your game code would go here
                break
            
            elif character_choice == "5":
                print("\nGoing back to main menu...")
                break
            
            else:
                print("\nInvalid choice! Please enter 1, 2, 3, 4, or 5.")
    
    elif choice == "2":
        print("\nThanks for playing! Goodbye!")
        break
    
    else:
        print("\nInvalid choice! Please enter 1 or 2.")