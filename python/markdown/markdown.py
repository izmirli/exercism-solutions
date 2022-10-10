"""Parses Markdown and returns the associated HTML."""
import re


def process_heading(md_line: str) -> tuple[bool, str]:
    """Check if a markdown heading line, and if so, translate to HTML.
    
    :param md_line: raw markdown line
    :return: is this a headingline, the HTML for given markdown
    """
    match_heading = re.match('(#{1,6}) (.*)', md_line)
    if not match_heading:
        return False, md_line

    heading_type = len(match_heading.group(1))
    return True, f"<h{heading_type}>{match_heading.group(2)}</h{heading_type}>"


def process_strong(md_line: str) -> str:
    """If theres bold markdown in given line, translate to HTML.
    
    :param md_line: raw markdown line
    :return: the HTML for given markdown
    """
    strong_match = re.match('(.*)__(.*)__(.*)', md_line)
    if not strong_match:
        return md_line
    
    return strong_match.group(1) + '<strong>' + strong_match.group(2) + '</strong>' + strong_match.group(3)
    

def process_em(md_line: str) -> str:
    """If theres italic markdown in given line, translate to HTML.
    
    :param md_line: raw markdown line
    :return: the HTML for given markdown
    """
    em_match = re.match('(.*)_(.*)_(.*)', md_line)
    if not em_match:
        return md_line
    
    return em_match.group(1) + '<em>' + em_match.group(2) + '</em>' + em_match.group(3)
    

def parse(markdown: str) -> str:
    md_lines = markdown.split('\n')
    html = ''
    in_list = False
    in_list_append = False
    for current_line in md_lines:
        heading, current_html = process_heading(current_line)
        if heading:
            html += current_html
            continue
        
        list_match = re.match(r'\* (.*)', current_line)
        if list_match:
            curr = list_match.group(1)
            curr = process_strong(curr)
            curr = process_em(curr)
            if not in_list:
                in_list = True
                current_line = '<ul><li>' + curr + '</li>'
            else:
                current_line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        non_p_match = re.match('<h|<ul|<p|<li', current_line)
        if not non_p_match:
            current_line = '<p>' + current_line + '</p>'

        current_line = process_strong(current_line)
        current_line = process_em(current_line)
        
        if in_list_append:
            current_line = '</ul>' + current_line
            in_list_append = False
        
        html += current_line
        
    if in_list:
        html += '</ul>'
    
    return html
