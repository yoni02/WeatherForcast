from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    api_key = '5f5218816375f19ff1b8476bf4a9906b'  # Replace with your actual API key from OpenWeather
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(weather_url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('index.html', weather=weather)
    else:
        error = "City not found!"
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
