from flask import Flask, request, jsonify
from flask_cors import CORS
from calendar_tool import book_meeting, check_availability

app = Flask(__name__)
CORS(app)

@app.route('/api/book_meeting', methods=['POST'])
def handle_booking():
    data = request.json
    print(f"\n🔔 [API REQUEST] Booking {data.get('title')} at {data.get('date_time')}")
    result = book_meeting(date_time_iso=data.get('date_time'), name=data.get('guest_email'))
    print(f"✅ [API RESPONSE] {result}")
    return jsonify({"result": result})

@app.route('/api/check_availability', methods=['POST'])
def handle_availability():
    data = request.json
    print(f"\n📅 [API REQUEST] Checking availability for {data.get('date')}")
    result = check_availability(date_iso=data.get('date'))
    print(f"✅ [API RESPONSE] {result}")
    return jsonify({"result": result})

if __name__ == '__main__':
    print("🚀 Local API Bridge running on http://127.0.0.1:5000")
    print("🚀 Nova AI Assistant running on http://localhost:8000")
    app.run(port=5000)