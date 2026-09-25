from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO 
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# 🔹 Initialize Flask-SocketIO
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        mobile = request.form.get('mobile', '').strip()
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        country = request.form.get('country', '').strip()
        pincode = request.form.get('pincode', '').strip()

        if name and mobile and city and state and country and pincode:
            session['logged_in'] = True
            session['user_info'] = {
                'name': name,
                'mobile': mobile,
                'city': city,
                'state': state,
                'country': country,
                'pincode': pincode
            }
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="All fields are required.")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    user_info = session['user_info']
    return render_template('dashboard.html', user_info=user_info)

bus_location = {"latitude": None, "longitude": None, "direction": None}

@app.route('/share-location')
def share_location():
    return render_template('ShareLocation.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    global bus_location
    data = request.json
    bus_location["latitude"] = data.get("latitude")
    bus_location["longitude"] = data.get("longitude")
    bus_location["direction"] = data.get("direction")

    # 🔹 Emit the update using socketio
    socketio.emit('bus_update', bus_location)

    return jsonify({"status": "updated", "location": bus_location})

@app.route('/get_location', methods=['GET'])
def get_location():
    return jsonify(bus_location)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
