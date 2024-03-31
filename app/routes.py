from app import app

from flask import render_template
from app.forms import InputForm
import re

@app.route('/', methods=(['GET', 'POST']))
def index():
    form = InputForm()
    if form.validate_on_submit():
        regex = form.regex.data
        test_string = form.test_string.data
        matches_as_list = re.findall(regex, test_string)
        matches_iter = re.finditer(regex, test_string)
        num_matches = len(matches_as_list)
        if not matches_as_list:
            match_result = 'No matches.'
        else:
            match_result = highlight_matches(matches_iter, test_string)
        match_list = list_of_matches(regex, test_string)
        captures = match_captures(regex, test_string)
        
        return render_template('index.html', form=form, 
                               match_result=match_result,
                               num_matches=num_matches,
                               match_list=match_list,
                               captures=captures)
    
    return render_template('index.html', form=form)


def highlight_matches(matches, string):
    matches = [m.group() for m in matches] # get list of matches out of iterator
    matches = set(matches) # removing duplicates
    for match in matches:
        regex = f"{match}"
        highlighted_matches = re.sub(regex, lambda x: "<span>"+x.group()+"</span>", string)
        string = highlighted_matches

    return highlighted_matches


def list_of_matches(regex, string):
    matches = re.finditer(regex, string)
    match_list = [(m.span(), m.group()) for m in matches]

    return match_list


def match_captures(regex, string):
    matches = re.finditer(regex, string)
    captures = [(m.groups(), num + 1) for num, m in enumerate(matches)]
    
    return captures
