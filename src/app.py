from flask import Flask, jsonify, request, render_template
from .quotes import get_random_quote, get_metrics  # relative import

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote", methods=["GET"])
def quote():
    category = request.args.get("category")
    q = get_random_quote(category)
    return jsonify(q)

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify(get_metrics())

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

