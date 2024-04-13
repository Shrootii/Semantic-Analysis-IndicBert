# from flask import Flask, request, jsonify
# from mahaNLP.sentiment import SentimentAnalyzer
# import json

# app = Flask(_name_)

# @app.route('/analyze-sentiment', methods=['POST'])
# def analyze_sentiment():
#     data = request.json
#     text = data.get('text')
#     language = data.get('language')
    
#     print(text)
#     print(language)
#     if text is None or language is None:
#         return jsonify({'error': 'Invalid request'}), 400

#     if language == "marathi":
#         model = SentimentAnalyzer()
#         result = model.get_polarity_score(text)
#         result_dict = result.to_dict(orient='records')
#         json_result = json.dumps(result_dict)
#         return jsonify({'result': json_result})
#     else:
#         return jsonify({'error': 'Unsupported language'}), 400

# if _name_ == "_main_":
#     app.run(debug=True)  # Run the Flask app in debug mode

from flask import Flask, request, jsonify
from flask_cors import CORS
from mahaNLP.sentiment import SentimentAnalyzer
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text')
    language = data.get('language')
    
    if text is None or language is None:
        return jsonify({'error': 'Invalid request'}), 400

    if language == "marathi":
        model = SentimentAnalyzer()
        result = model.get_polarity_score(text)
        result_dict = result.to_dict(orient='records')
        json_result = json.dumps(result_dict)
        response = jsonify({'result': json_result})
        response.headers.add('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        return response
    else:
        return jsonify({'error': 'Unsupported language'}), 400

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode