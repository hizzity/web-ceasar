from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
                           # is form = """ in correct spot
form =                                                                       
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
       <form action="/" method="gett">
                <label for="rot">Rotate by:</label>                                       
                <input value = '0' type="text" name="rot"/>            
                <br>
                <input id= type="textarea" name="text" size = "textarea"/>         <!-- how to use 'textarea' above -->
                <br>
                <input type="submit" value = "Submit Query"/>
    </body>
</html>




@app.route("/", methods=['get'])                        ## how use form.format(...)
def index():
    return form.format(form)

@app.route("/", methods=['get'])                           ## change to 'post' request
def encrypt(text, rot):                                   ## how to pull user input for rot and text from form
    rotation = int(rot)
    encrypted_text = rotate_string(text, rotation)
    return """                                                          
    <html>                                                  <! how use form.format(...)
        <h1> encrypted_text </h1>
    </html>
    """

app.run()