from app import app

from flask import render_template
# import re

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# def process_inputs():
#     if request.method == "POST":
#         regex = request.form["test-regex"]
#         test_string = request.form['test-string']

#         found_matches = find_matches(regex, test_string)
        
#         return render_template('index.html', 
#                                found_matches=found_matches)
    
#     else:
#         return render_template('index.html', output="")
        
# def find_matches(regex, test_string):
#     return re.findall(regex, test_string)