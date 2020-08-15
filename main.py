class HtmlDocument:
    #that lets you initialize some HTML for a new document.
    def __init__(self,name):
        self.name = name

class HtmlMananger:
    #that defines functions that let you create a new HTML document, 
    # and save the document to your files.
    # write-html.py
    def create_html():
        f = open('dolma.html','w')
        message = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        f.write(message)
        f.close()

    create_html()

# class AWSManager:
#     #defines the connections to boto3 and some functions that let you save your file to S3.