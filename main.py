from flask import Flask
import threading
import subprocess
import os

app = Flask(__name__)

def run_hermes():
    subprocess.Popen(["bash", "-c", "export PATH=$HOME/.local/bin:$PATH && hermes gateway run"])

@app.route('/')
def home():
    return "✅ Hermes Agent is running!"

@app.route('/status')
def status():
    return "alive"

if __name__ == "__main__":
    threading.Thread(target=run_hermes, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
