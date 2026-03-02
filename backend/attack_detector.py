import time

request_times = []

def detect_attack():

    current_time = time.time()

    request_times.append(current_time)

    # Keep last 5 seconds
    request_times[:] = [
        t for t in request_times
        if current_time - t < 5
    ]

    print("Requests in last 5 seconds:", len(request_times))

    # Lower threshold for testing
    if len(request_times) >= 5:
        return True

    return False