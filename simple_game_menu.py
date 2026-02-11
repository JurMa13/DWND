while True:
    # Main Menu
    print("\n========== MAIN MENU ==========")
    print("1. New Game")
    print("2. Quit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        # Difficulty Selection Menu
        while True:
            print("\n===== CHOOSE DIFFICULTY =====")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Impossible")
            print("5. Back")

            difficulty_choice = input("Choose difficulty (1-5): ")
            
            if difficulty_choice == "1":
                print("\nStarting game in Easy difficulty!")
                break
            
            elif difficulty_choice == "2":
                print("\nStarting game in Medium difficulty!")
                break
            
            elif difficulty_choice == "3":
                print("\nStarting game in Hard difficulty!")
                break
            
            elif difficulty_choice == "4":
                print("\nStarting game in Impossible difficulty!")
                break
            
            elif difficulty_choice == "5":
                print("\nGoing back to main menu...")
                break
            
            else:
                print("\nInvalid choice! Please enter 1, 2, 3, 4, or 5.")
    
    elif choice == "2":
        print("\nThanks for playing! Goodbye!")
        break
    
    else:
        print("\nInvalid choice! Please enter 1 or 2.")