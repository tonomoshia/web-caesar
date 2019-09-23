from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
           <form action = "/" method="POST">
                <label for="rot">Rotate by:</label>
                <input type ="text" name ="rot" id="rot" value="0" />
                <input type="textarea" name ="text" rows="4" cols="50" />
                <input type="submit" value="Encrypt"/>
            </form>
        </body>
    </html>
"""
@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = str(request.form['text'])
    encrypted_text = rotate_string(message, rot)
    return form.format(encrypted_text)

app.run()
