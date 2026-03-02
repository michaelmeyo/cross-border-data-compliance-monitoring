import hashlib

SECRET_KEY = "CYBERLAB_SECRET_KEY_2026"

def generate_signature(data_string):
    combined = data_string + SECRET_KEY
    signature = hashlib.sha256(combined.encode()).hexdigest()
    return signature

def verify_signature(data_string, received_signature):
    expected_signature = generate_signature(data_string)
    return expected_signature == received_signature