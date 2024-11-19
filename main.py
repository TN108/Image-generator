from flask import Flask, jsonify
#from config import key
import openai
from flask import render_template

openai.api_key = "Your open Api Key"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/templates/about')
def about():
    return render_template('about.html')



@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
  print(response)
  return jsonify(response)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
