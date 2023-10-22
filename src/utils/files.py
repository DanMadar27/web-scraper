from os import path
from datetime import datetime
import pdfkit

def modification_time(file_path):
    if not path.exists(file_path):
        return None
    
    modification_time = path.getmtime(file_path)
    modification_datetime = datetime.fromtimestamp(modification_time)
    return modification_datetime

"""
html: html string
output: output file path
"""
def html_to_pdf(html, output, title):
    html = '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {
                        padding: 15px;
                        font-family: 'Arial';
                        line-height: 110%;
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
                html + \
            '</body>' + \
        '</html>'

    pdfkit.from_string(html, output)