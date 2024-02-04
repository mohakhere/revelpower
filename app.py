from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate_ghi', methods=['POST'])
def calculate_ghi():
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    date = request.form['date']
    tilt = float(request.form['tilt'])
    azimuth = float(request.form['azimuth'])

    api_url = 'http://api-server:5000/calculate_ghi'
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'date': date,
        'tilt': tilt,
        'azimuth': azimuth,
    }
    response = requests.post(api_url, json=payload)
    result = response.json()
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
