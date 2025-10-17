from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meditation')
def meditation():
    return render_template('meditation.html')

@app.route('/counseling')
def counseling():
    return render_template('counseling.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['message'].lower()
    responses = {
        "stress": {
            "text": "Take a slow, deep breath... inhale for 4 seconds, hold, and exhale. You’re doing great.",
            "context": "Try repeating this breathing exercise 5 times to reduce stress quickly."
        },
        "anxiety": {
            "text": "You are not alone. Try grounding yourself—notice 5 things you can see and 4 you can touch.",
            "context": "Grounding techniques help bring your focus back to the present moment."
        },
        "sad": {
            "text": "Everyone has difficult days. Maybe a short meditation will help—it’s available in the MindSpace meditation section.",
            "context": "Meditation promotes calm and helps manage feelings of sadness."
        },
        "happy": {
            "text": "That's wonderful to hear! Keep cherishing these joyful moments.",
            "context": "Enjoy the positive energy—it’s good for mental wellness."
        },
        "lonely": {
            "text": "Feeling lonely can be tough. Remember, MindSpace is here for you anytime.",
            "context": "Connecting through conversation or community can help ease loneliness."
        },
        "angry": {
            "text": "It's okay to feel anger. Try a quick physical activity or deep breathing to calm down.",
            "context": "Expressing anger safely is important for emotional health."
        },
        "tired": {
            "text": "If you're feeling tired, it might be helpful to rest or take a short break.",
            "context": "Self-care and rest are vital to maintaining your mental health."
        },
        "bye": {
        "text": "Thank you for relaxing with MindSpace. Have a great day!",
        "context": "Remember, you can come back anytime you need support."
    }
    }
    default_response = {
        "text": "Hello! I am here to support you. Please tell me how you're feeling.",
        "context": "Sharing your feelings can be the first step towards feeling better."
    }
    response = responses.get(user_input, default_response)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)

