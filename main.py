from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }

                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
        </style>
        <body>
            <form method="POST">
                <label for="rotation">Rotate by:</label>
                <input id="rotation" type="text" name="rot" value="0">
                <textarea name="text"></textarea>
                <input type="submit">
            <!-- form goes here -->
        </body>
    </html>
    """


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def rotate_str():
    rot = int(request.form['rot'])
    text = request.form['text']

    return '<h1>' + str(encrypt(text, rot)) + '</h1>'

# the error code being debugged at this time: new_position = (alphabet_position(char) + rot)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
     


app.run()