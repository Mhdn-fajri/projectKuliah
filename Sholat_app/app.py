from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_prayer_times(city):
    url = f"https://api.aladhan.com/v1/timingsByCity"
    params = {
        'city': city,
        'country': 'Indonesia',
        'method': 2  # Metode Umm al-Qura
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['code'] == 200:
        timings = data['data']['timings']
        hijri_date = data['data']['date']['hijri']
        return timings, hijri_date
    else:
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    city = 'Jakarta'
    if request.method == 'POST':
        city = request.form.get('city')
    
    prayer_times, hijri_date = get_prayer_times(city)
    return render_template(
        'index.html',
        city=city,
        prayer_times=prayer_times,
        hijri_date=hijri_date
    )

if __name__ == '__main__':
    app.run(debug=True)
