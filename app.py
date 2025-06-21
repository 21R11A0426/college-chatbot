# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime 
import os
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all routes

OWM_API_KEY = "c8e4d4dfe1132b18698dc91a8e05c799"


# Example Timetable
timetable = {
    "monday": ["EMI", "MWE", "OC", "MWE LAB-A2/EDA LAB-A1"],
    "tuesday": ["EMI", "IOT", "OC", "MWE", "GB", "MWE"],
    "wednesday": ["IOT", "IOT", "MWE", "GB", "GB", "MWE"],
    "thursday": ["OC", "MWE", "IOT", "GB", "MWE"],
    "friday": ["WIPRO TRAINING PROGRAM"],
    "saturday": ["WIPRO TRAINING PROGRAM"],
    "sunday": ["HoliDay"]
}

# College Information
college_info = {
    "name": "Gitanjali College of Engineering & Technology",
    "location": "Hyderabad, Telangana",
    "branches": [
        "B.Tech in Computer Science",
        "Electronics & Communication",
        "Electrical Engineering",
        "Information Technology",
        "CSE sub branches",
        "AI ML DS Cyber Security",
        "Mechanical and Civil"
    ],
    "chairman": "sri G.R.Ravindar Reddy",
    
    # **Added Information**
    "principal": "Dr. Uday Kumar Susurala",
    "hod": "Dr. G Sree Lakshmi",
    "dean": "Dr. Hari Kumar",
    "placements": {
        "2024": 1410,
        "2023": 1328,
        "2022": 1507
    },
    "clubs": [
        "StuVibe",
        "Alumni",
        "nt Up",
        "Dopy",
        "Res",
        "NEN",
        "CDC",
        "DECO"
    ],
    "fests": [
        "StuVibe",
        "Alumni",
        "nt Up",
        "Dopy",
        "Res",
        "NEN",
        "CDC",
        "DECO"
    ]
}

# Function to generate bot response
def generate_response(user_input):
    user_input = user_input.lower()
    
    # Greetings
    if "hello" in user_input:
        return "Hello, how may I assist you today?"
    elif any(greet in user_input for greet in ["good morning", "good afternoon", "good evening"]):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            greeting = "Good morning!"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
        return f"{greeting} How may I assist you today?"
    
    # Chatbot Explanation
    elif "chatbot" in user_input:
        return ("A chatbot is a computer program or an artificial intelligence (AI) "
                "that simulates human conversation or interaction through text or voice.")
    
    # Weather Information
    elif "weather" in user_input:
        return get_weather()
    
    # Time Inquiry
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    # Location Inquiry
    elif "location" in user_input:
        return "You are currently in Hyderabad city."
    
    # Classes Inquiry
    elif "classes" in user_input:
        today = datetime.datetime.now().strftime("%A").lower()
        if "today" in user_input:
            if today in timetable:
                classes = ", ".join(timetable[today])
                return f"Your classes for today are: {classes}."
            else:
                return "There are no classes scheduled for today."
        else:
            for day in timetable:
                if day in user_input:
                    classes = ", ".join(timetable[day])
                    return f"Your classes for {day.capitalize()} are: {classes}."
            return "I'm sorry, I didn't understand that."
    
    # College Information Inquiry
    elif "gitanjali college" in user_input:
        return ("Sure, I can provide information about Gitanjali College. "
                "You can ask about: branches, chairman, principal, placements, clubs, fests, or location.")
    
    elif "college location" in user_input:
        return f"The college is located in {college_info['location']}."
    
    elif "branches" in user_input:
        branches = ", ".join(college_info["branches"])
        return f"The branches offered are: {branches}."
    
    elif "chairman" in user_input:
        return f"The chairman of the college is {college_info['chairman']}."
    
    # **New Responses Added Below**
    
    # Principal Inquiry
    elif "principal" in user_input:
        principal = college_info.get("principal", "Principal information not available.")
        return f"The principal of Gitanjali College is {principal}."
    
    # HOD and Dean of ECE Inquiry
    elif "hod" in user_input:
        hod_ece = college_info.get("hod", "HOD of ECE information not available.")
        return f"The HOD of ECE is {hod_ece}."
    elif "dean" in user_input:
        dean_ece = college_info.get("dean", "Dean of ECE information not available.")
        return f"The Dean of ECE is {dean_ece}."
    
    # Placements Inquiry
    elif "placements" in user_input:
        placements = college_info.get("placements", {})
        if placements:
            response = "Here are the placement statistics:\n"
            for year, count in placements.items():
                response += f"- {year} batch: {count} placements\n"
            return response.strip()
        else:
            return "Placement information is currently unavailable."
    
    # Clubs Inquiry
    elif "clubs" in user_input:
        clubs = college_info.get("clubs", [])
        if clubs:
            clubs_list = ", ".join(clubs)
            return f"The clubs in Gitanjali College are: {clubs_list}."
        else:
            return "No clubs information is available at the moment."
    
    # Fests Inquiry
    elif "fests" in user_input:
        fests = college_info.get("fests", [])
        if fests:
            fests_list = ", ".join(fests)
            return f"The fests in Gitanjali College are: {fests_list}."
        else:
            return "No fests information is available at the moment."
    
    # Goodbye
    elif "goodbye" in user_input or "bye" in user_input:
        return "Thank you! Visit again for more details!"
    
    # Unrecognized Input
    else:
        return "I'm sorry, I didn't understand that."

# Function to get weather information (Placeholder)
def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Hyderabad,IN",
        "appid": OWM_API_KEY,
        "units": "metric",
        "lang": "en"
    }
    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        temp     = data["main"]["temp"]
        desc     = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_kmh = data["wind"]["speed"] * 3.6  # m/s → km/h

        return (f"Hyderabad: {temp:.1f}°C, {desc}, "
                f"Humidity {humidity}%, Wind {wind_kmh:.1f} km/h.")
    except requests.RequestException as e:
        print("Weather API error:", e)
        return "Sorry, I couldn't fetch the weather right now."
   

# Route to render the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot messages
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400
        response = generate_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error in /chat: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
