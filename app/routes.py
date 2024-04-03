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
        flag_ignorecase = form.flag_ignorecase.data
        flag_multiline = form.flag_multiline.data
        flag_dotall = form.flag_dotall.data
        flags = flag_args(flag_ignorecase, flag_multiline, flag_dotall)
        matches_as_list = re.findall(regex, test_string, *flags)
        matches_iter = re.finditer(regex, test_string, *flags)
        num_matches = len(matches_as_list)
        if not matches_as_list:
            match_result = 'No matches.'
        else:
            match_result = highlight_matches(matches_iter, test_string)
        match_list = list_of_matches(regex, test_string, *flags)
        captures = match_captures(regex, test_string, *flags)
        
        return render_template('index.html', form=form, 
                               flags=flags,
                               match_result=match_result,
                               num_matches=num_matches,
                               match_list=match_list,
                               captures=captures)
    
    return render_template('index.html', form=form)


def flag_args(flag_ignorecase, flag_multiline, flag_dotall):
    if not flag_ignorecase and not flag_multiline and not flag_dotall:
        return []
    elif flag_ignorecase and not flag_multiline and not flag_dotall:
        return [re.I]
    elif flag_ignorecase and flag_multiline and not flag_dotall:
        return [re.I | re.M]
    elif flag_ignorecase and not flag_multiline and flag_dotall:
        return [re.I | re.S]
    elif flag_ignorecase and flag_multiline and flag_dotall:
        return [re.I | re.M | re.S]
    elif not flag_ignorecase and flag_multiline and not flag_dotall:
        return [re.M]
    elif not flag_ignorecase and flag_multiline and flag_dotall:
        return [re.M | re.S]
    else:
        return [re.S] 


def highlight_matches(matches, string):
    matches = [m.group() for m in matches] # get list of matches out of iterator
    matches = list(set(matches)) # removing duplicates
    matches = [match if match != "." else "\." for match in matches ] # escaping 'dot' if it is a match
    for match in matches[:10]: 
        regex = f"{match}"
        highlighted_matches = re.sub(regex, lambda x: "<span>"+x.group()+"</span>", string)
        string = highlighted_matches

    return highlighted_matches


def list_of_matches(regex, string, *flags):
    matches = re.finditer(regex, string, *flags)
    match_list = [(m.span(), m.group()) for m in matches]

    return match_list


def match_captures(regex, string, *flags):
    matches = re.finditer(regex, string, *flags)
    captures = [(m.groups(), num + 1) for num, m in enumerate(matches)]

    if sum([len(capture[0]) for capture in captures]) == 0: 
        return None
    else: 
        return captures
    

@app.route('/reference')
def reference():
    return render_template('reference.html')