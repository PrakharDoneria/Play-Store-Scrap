from flask import Flask, jsonify, request, redirect
import play_scraper

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def app_details():
    app_id = request.args.get('id')
    if not app_id:
        return jsonify({"error": "App ID is required"}), 400

    try:
        app_details = play_scraper.details(app_id)
        return jsonify(app_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
