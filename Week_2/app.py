from tools import get_weather, get_news

def main():
    print("\n🌟 SMART WEATHER & NEWS ASSISTANT 🌟")

    while True:
        print("\n==============================")
        print("1️⃣ Weather Info")
        print("2️⃣ Latest News")
        print("3️⃣ Exit")
        print("==============================")

        choice = input("👉 Enter choice (1/2/3): ")

        if choice == "1":
            city = input("\n🌍 Enter city name: ")
            print("\n" + get_weather(city))

        elif choice == "2":
            print("\n⏳ Fetching latest news...\n")
            print(get_news())

        elif choice == "3":
            print("\n👋 Goodbye! Stay updated.")
            break

        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()