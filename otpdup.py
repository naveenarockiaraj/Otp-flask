from flask import Flask, request, jsonify
from twilio.rest import Client
import random
import os

app = Flask(__name__)

TWILO_ACCOUNT_SID = 'reffer obsidean notes'
TWILO_AUTH_TOKEN = 'reffer obsedian notes'
TWILO_PHONE_NUMBER = 'reffer obsidean notes'

client = Client(TWILO_ACCOUNT_SID, TWILO_AUTH_TOKEN)

otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    message = client.messages.create(
        body=f"Your OTP is {otp}.",
        from_=TWILO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid

@app.route('/send_otp', methods=['POST'])
def send_otp_route():
    data = request.get_json()
    phone_number = data.get('phone_number')

    otp = generate_otp()
    send_otp(phone_number, otp)

    otp_storage[phone_number] = otp

    return jsonify({'message': 'OTP send'}), 200

@app.route('/verify_otp', methods=['POST'])
def verify_otp_route():
    data = request.get_json()
    phone_number = data.get('phone_number')
    otp = data.get('otp')

    stored_otp = otp_storage.get(phone_number)

    if stored_otp and otp == stored_otp:
        return jsonify({'message': 'OTP verified'}), 200
    else:
        return jsonify({'message': 'Invalid OTP'}), 400

if __name__ == '__main__':
    app.run(debug=True)