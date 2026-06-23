import requests

# ---------------- WEATHER ----------------
def get_weather(city):
    try:
        api_key = "266c19e5ec8c5fbce117b0d659eeb8d5"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            return f"""
🌍 City: {city.title()}
🌡 Temperature: {data['main']['temp']}°C
🌤 Weather: {data['weather'][0]['description']}
💧 Humidity: {data['main']['humidity']}%
"""
        else:
            return f"❌ Weather Error: {data.get('message', 'Unknown error')}"

    except Exception as e:
        return f"❌ Error: {e}"


# ---------------- NEWS ----------------
def get_news():
    try:
        api_key = "9a1ce8d9455d43c78987d72cd22edbe1"

        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get("status") == "ok":
            articles = data.get("articles", [])

            if not articles:
                return "⚠️ No news found."

            news = "\n".join([f"📰 {a['title']}" for a in articles[:5]])
            return f"\n🔥 Top Headlines:\n{news}"

        else:
            return f"❌ News Error: {data.get('message', 'Unknown error')}"

    except Exception as e:
        return f"❌ Error: {e}"