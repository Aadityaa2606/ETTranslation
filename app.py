from flask import Flask, request, jsonify, send_from_directory
import threading
import time
import os

from translator import language_translator

app = Flask(__name__)

# Dictionary to store results of translations
results = {}

# Serve the HTML file from the root URL
@app.route('/')
def serve_html():
    return send_from_directory(os.getcwd(), 'index.html')

# Endpoint to start translation
@app.route('/translate', methods=['POST'])
def translate():
    # Get input text from the request
    data = request.get_json()
    text = data.get('text')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Generate a unique job ID for this translation task
    job_id = str(int(time.time() * 1000))

    # Run translation in a separate thread to avoid blocking
    thread = threading.Thread(target=run_translation, args=(job_id, text))
    thread.start()

    return jsonify({'message': 'Translation started', 'job_id': job_id}), 202

# Helper function to perform translation and store result
def run_translation(job_id, text):
    # Perform the translation
    result = language_translator(text)
    
    # Store the result in the results dictionary with job_id as key
    results[job_id] = result

# Endpoint to check result of translation by job ID
@app.route('/translate/result/<job_id>', methods=['GET'])
def get_translation_result(job_id):
    result = results.get(job_id)
    if result is None:
        return jsonify({'status': 'pending'}), 202
    return jsonify({'status': 'completed', 'result': result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
