import pdfkit

def htmlToPdf(html, output):
    """
    html: html string
    output: output file path
    """

    html = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: 'Arial';
                        line-height: 110%;
                        letter-spacing: 1px;
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
            <body>''' + html + '</body>' + '''
        </html>'''

    pdfkit.from_string(html, output)