from flask import Flask, request, jsonify
import datetime
import json

from compliance_engine import evaluate_transfer, log_transfer
from attack_detector import detect_attack
from ml_detector import detect_anomaly
from security_utils import verify_signature

VALID_API_KEY = "CYBERLAB_SECURE_2026"

app = Flask(__name__)


@app.route('/transfer', methods=['POST'])
def transfer_data():

    # 1️⃣ API KEY AUTHENTICATION
    api_key = request.headers.get("X-API-KEY")

    if api_key != VALID_API_KEY:
        return jsonify({
            "error": "Unauthorized access"
        }), 401

    # 2️⃣ GET JSON DATA
    data = request.json

    # 3️⃣ SIGNATURE VERIFICATION
    received_signature = request.headers.get("X-SIGNATURE")

    payload_string = json.dumps(data, sort_keys=True)

    if not verify_signature(payload_string, received_signature):
        return jsonify({
            "error": "Data integrity check failed"
        }), 400

    # 4️⃣ RULE-BASED ATTACK DETECTION
    attack = detect_attack()

    if attack:
        return jsonify({
            "warning": "Possible attack detected"
        }), 403

    # 5️⃣ ML-BASED ANOMALY DETECTION
    request_count = len(detect_attack.__globals__['request_times'])

    ml_attack = detect_anomaly(request_count)

    if ml_attack:
        return jsonify({
            "warning": "ML detected abnormal traffic"
        }), 403

    # 6️⃣ COMPLIANCE EVALUATION
    data["timestamp"] = str(datetime.datetime.now())

    risk, issues = evaluate_transfer(data)

    log_transfer(data, risk, issues)

    response = {
        "risk_score": risk,
        "issues": issues
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000)