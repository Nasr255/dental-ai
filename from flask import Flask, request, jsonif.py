from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_KEY"

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    image_base64 = data.get("image")

    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # هذا يدعم الصور
        messages=[
            {"role": "system", "content": "You are a dentist AI diagnosing dental images."},
            {"role": "user", "content": [
                {"type": "text", "text": "Please analyze this dental image and give diagnosis:"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"}
            ]}
        ]
    )

    diagnosis = response.choices[0].message.content
    return jsonify({"diagnosis": diagnosis})

if name == "__main__":
    app.run(host="0.0.0.0", port=5000)s