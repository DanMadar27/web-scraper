from os import path
from datetime import datetime
import pdfkit

def modification_time(file_path):
    if not path.exists(file_path):
        return None
    
    modification_time = path.getmtime(file_path)
    modification_datetime = datetime.fromtimestamp(modification_time)
    return modification_datetime

# Convert html string to styled html
def str_to_html(html, title, date):
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {
                        padding: 15px;
                        font-family: 'Arial';
                        letter-spacing: 1px;
                    }

                    h1 {
                        margin: 15px 0;
                    }

                    ul {
                        padding: 15px;
                    }

                    li {
                        margin: 15px 0;
                        padding: 15px;
                    }
                </style>
            </head>
            <body>''' + \
                '<h1>' + title + '</h1>' + \
                '<h2>' + date + '</h2>' + \
                html + \
            '</body>' + \
        '</html>'

"""
html: html string
output: output file path
title: title of the file
date: date of the file
"""
def html_to_pdf(html, output, title, date):
    html = str_to_html(html, title, date) # Create styled html
    pdfkit.from_string(html, output)