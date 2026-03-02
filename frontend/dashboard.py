from flask import Flask
import os

app = Flask(__name__)

LOG_FILE = "C:\\Users\\machm\\CyberLab\\logs\\system.log"


@app.route('/')
def dashboard():

    total = 0
    compliant = 0
    noncompliant = 0

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as file:

            content = file.read()

            entries = content.split("------------------------")

            for entry in entries:

                if "Risk Score" in entry:

                    total += 1

                    if "Status: COMPLIANT" in entry:
                        compliant += 1

                    if "Status: NON-COMPLIANT" in entry:
                        noncompliant += 1

    html = f"""

    <h1>CyberLab Security Dashboard</h1>

    <h2>Statistics</h2>

    Total Transfers: {total} <br>
    Compliant Transfers: {compliant} <br>
    Non-Compliant Transfers: {noncompliant} <br>

    <br><br>

    <h2>System Status</h2>

    Compliance Engine: ACTIVE <br>
    Attack Detection: ACTIVE <br>

    """

    return html


if __name__ == '__main__':
    app.run(port=5001)