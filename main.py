from flask import Flask, render_template, request, jsonify

from LeTECia import get_response



app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("dplymnt.html")


@app.post("/predict")
def predict():
   text = request.get_json().get("message")
   response = get_response(text)
   message = {"answer": response}
   return jsonify(message)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 3000)),host='0.0.0.0',debug=True)
