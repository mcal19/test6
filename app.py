from flask import Flask, request
import g4f
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    input = request.form.get('inputt')


    response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": input],
    ) 


    #response = g4f.ChatCompletion.create(
    #model=g4f.models.default,
    #messages=[{"role": "user", "content": input}],
    #timeout=120,
    #)

    return "RESPONSE: " + str(response)
