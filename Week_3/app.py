from memory import save_preference, search_preference


print("   PERSONAL MEMORY ASSISTANT")


while True:

    print("\nChoose an option:")
    print("1. Save Preference")
    print("2. Search Preference")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        text = input("Enter preference: ")
        save_preference(text)
        print("✅ Preference Saved!")

    elif choice == "2":
        query = input("Search: ")

        results = search_preference(query)

        if len(results) > 0:
            print("\nFound Preferences:")
            for item in results:
                print("-", item)
        else:
            print("No preference found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")