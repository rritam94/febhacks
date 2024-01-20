from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
import chatbot
import findoctors

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

count = 0

@app.route('/entrance', methods=['POST'])
@cross_origin()
def entrance():
    data = request.get_json()
    print(data)
    return jsonify({
        'ai_message': chatbot.generate_response(data['message'] + ". Use only 2-3 sentences in your response.")
    })

@app.route('/doctors', methods=['GET'])
@cross_origin()
def get_docs():
    global count
    doctors = []
    print(count)
    findoctors.search('optometrist')
    
    return jsonify({
        'doctors': doctors
    })

if __name__ == '__main__':
    app.run()