import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return "Hello CI -> Render!"

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # RenderはPORT環境変数を渡す（ローカルは5000でOK）
    port = int(os.getenv("PORT", "5001"))
    app.run(host="0.0.0.0", port=port)
