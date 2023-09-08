from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

curr_day = datetime.utcnow().strftime("%A")
curr_time = datetime.utcnow().strftime('%H:%M:%S %p UTC')

info = {
    "slack_name": "Obinna Anya",
    "current_day": "Thursday",
    "utc_time": "2023-08-21T15:04:05Z",
    "track": "backend",
    "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
    "github_repo_url": "https://github.com/username/repo",
    'status_code': 200
  }

@app.route('/')
def main() -> str:
  return 'Hello There!'

@app.route('/api', methods=['GET'])
def get_info():
  name = request.args.get('slack_name')
  track = request.args.get('track')

  response_data = {}

  if name and track:
    response_data['slack_name'] = name
    response_data['track'] = track
  else:
    response_data = info

  return jsonify(response_data)

if __name__ == '__main__':
  app.run(debug=True)
