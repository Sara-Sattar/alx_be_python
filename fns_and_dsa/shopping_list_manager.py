def main():
    shopping_list = []  

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print(f"{item} not found.")
        elif choice == 3:
            if shopping_list:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()
