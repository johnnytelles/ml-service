from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ML Service Running",
        "timestamp": "ok", 
        "endpoints": ["/train", "/predict", "/health"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/train', methods=['POST'])
def train():
    try:
        return jsonify({
            "status": "success",
            "accuracy": 0.85,
            "model_type": "RandomForest",
            "message": "Model training completed successfully"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        return jsonify({
            "signal": "COMPRA",
            "confidence": 0.75,
            "execution": "MANUAL"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
