from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ussd', methods=['GET', 'POST'])
def ussd():
    text = request.values.get("text", "")
    
    if text == "":
        return "CON Siri ya Wakulima\n1. Swahili\n2. English"
    elif text == "1":
        return "CON Sema tatizo lako kwa sauti (8 sekunde):"
    elif text == "2":
        return "CON Describe your farm problem in voice (8 seconds):"
    else:
        return "END Asante! Tutakurudia kwa jibu."

@app.route('/')
def home():
    return "Siri ya Wakulima Backend - OK"

# ONLY run app if executed directly (not on Render)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)