from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
                           
form =  """                                                                     
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
       <form action="" method='post'>
                <label for="rot">Rotate by:                                     
                <input value = '0' id ="rot" type="text" name="rot"/> 
                </label>             
                <br>
                <textarea class = "textarea" name="text"/>  
                {0}    
                </textarea>
                
                <br>
                <input type="submit" value = "Submit Query"/>
        </form>
    </body>
</html>
"""




@app.route("/", methods=['POST'])                           ## change to 'post' request
def encrypt():                                   ## how to pull user input for rot and text from form
    rotation = int(request.form["rot"])
    text = request.form["text"]
    encrypted_text = rotate_string(text, rotation)
    return form.format(encrypted_text)                   ##<h1> ???                                   
    

@app.route("/", methods=['get'])                        ## how use form.format(...)
def index():
    return form.format("")


app.run()