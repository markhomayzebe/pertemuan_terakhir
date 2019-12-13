import flask
import requests
import json
API_URL='http://localhost:8000'
app = flask.Flask(__name__)

@app.route('/')
def index():
    stats = requests.get(f'{API_URL}/api/v1/stats')
    hasil = 'Data belum berhasil diakses'
    if stats.status_code == 200:
        stats = json.loads(stats.text)
        hasil = f'Terdapat{len(stats)} data'
        return hasil
