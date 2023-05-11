import random
import requests
from flask import Flask

app = Flask(__name__)

# Access token for your Facebook app
ACCESS_TOKEN = '4638f14b390639f32d532f2fea977c1b'

# Page ID where you want to post the lyrics
PAGE_ID = '795072212051508'

# List of Lorde lyrics
LYRICS = [
    "We don't care; we're driving Cadillacs in our dreams",
    "We don't care; we aren't caught up in your love affair",
    "Let me live that fantasy",
    # Add more lyrics here
]

def post_lyric():
    # Select a random Lorde lyric
    random_lyric = random.choice(LYRICS)

    # Create the API endpoint URL
    url = f'https://graph.facebook.com/{795072212051508}/feed'

    # Construct the request parameters
    params = {
        'access_token': ACCESS_TOKEN,
        'message': random_lyric
    }

    # Send the POST request to post the lyric on Facebook
    response = requests.post(url, params=params)

    if response.status_code == 200:
        print('Lyric posted successfully.')
    else:
        print('Error posting lyric.')

# Route to trigger the bot manually (optional)
@app.route('/post_lyric')
def trigger_post_lyric():
    post_lyric()
    return 'Lyric posted.'

if __name__ == '__main__':
    # Run the bot every hour
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_lyric, 'interval', hours=1)
    scheduler.start()

    # Run the Flask app
    app.run()
