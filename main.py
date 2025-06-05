import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")  # Replace with your actual key

def generate_prompt(essay_type, topic, draft):
    if essay_type == "ECA":
        return f"Assume you are applying for Ivy League admission. Now you have to modify your ECA description from the common app. A draft is given. Edit and polish the following ECA (Extracurricular Activity) description to be concise, impressive, and emotional. No metter how long the draft is, must keep it under 150 characters. Topic: {topic}. Draft: {draft} Don't write any additional thing or ask anything without the main part!"
    elif essay_type == "CommonApp":
        return f"Assume you are applying for Ivy League admission. Now you have to modify your common app essay. A draft is given. Edit and enhance the following Common App personal essay for Ivy League admission. Make it deeply emotional and unique. No metter how long or short the draft is, must keep it in 500-650 words. Topic: {topic}. Draft: {draft} Don't write any additional thing or ask anything without the main part!"
    elif essay_type == "College":
        return f"Assume you are applying for Ivy League admission. Now you have to modify your college specific essay. Polish the following College Specific Essay for Ivy League admission. Focus on clarity, depth, and emotional engagement. Topic: {topic}. Draft: {draft} Don't write any additional thing or ask anything without the main part!"
    else:
        return "Invalid essay type."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polish_essay', methods=['POST'])
def polish_essay():
    data = request.get_json()
    essay_type = data.get('type')
    topic = data.get('topic')
    draft = data.get('draft')

    if not essay_type or not topic or not draft:
        return jsonify({"error": "All fields are required"}), 400

    prompt = generate_prompt(essay_type, topic, draft)

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192"  # ✅ Use correct Groq model name
        )
        result = response.choices[0].message.content.strip()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)




#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