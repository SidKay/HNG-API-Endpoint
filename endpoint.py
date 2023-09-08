from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def main() -> str:
  return 'Hello There!'

@app.route('/api', methods=['GET'])
def get_info():
  name = request.args.get('slack_name')
  track = request.args.get('track')

  response_data = {}

  if name and track:
    response_data = {
        "slack_name": "Obinna Anya",
        "current_day": datetime.utcnow().strftime("%A"),
        "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": "backend",
        "github_file_url": "https://github.com/SidKay/HNG-API-Endpoint/blob/main/endpoint.py",
        "github_repo_url": "https://github.com/SidKay/HNG-API-Endpoint",
        'status_code': 200
    }

  return jsonify(response_data)

if __name__ == '__main__':
  app.run(debug=True)
