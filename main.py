from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
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
    </head>
    <body>
       <form action="/" method="post"/>
                <label for="rot">Rotate by:</label>         <!how set default to 0/>
                <input id= type="text" name="rot"/>              <!##what for id?/>
                <input id= type="textarea" name="text"/>         <!##what for id?/>
                <input type="Submit Query"/>
    </body>
<html>
"""



@app.route("/", methods=["POST"])
def index():
    return form

app.run()