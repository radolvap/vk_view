from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewers')
def viewer_count():
    video_url = request.args.get('v')
    if not video_url:
        return "No video URL provided", 400

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(video_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        viewer_elem = soup.find('span', class_='mv_views')
        count = viewer_elem.text.strip() if viewer_elem else "Offline"

        return f"""
        <html>
        <head>
            <meta http-equiv='refresh' content='10'>
        </head>
        <body style='background: transparent; color: white; font-size: 40px; font-family: Arial;'>
            👁 {count}
        </body>
        </html>
        """
    except Exception as e:
        return f'<html><body style="color: red;">Ошибка: {e}</body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
