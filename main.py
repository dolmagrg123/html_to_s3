import boto3

class HtmlDocument:
    #that lets you initialize some HTML for a new document.
    def __init__(self,content):
        self.content = content

class HtmlMananger:
    #that defines functions that let you create a new HTML document, 
    # and save the document to your files.
    # write-html.py

    def __init__(self):
        self.document = None

    def create_html(self):
        
        message = """<html>
        <head>This is a new html file</head>
        <h1> My name is Dolma </h1>
        <body>
        <p> My name is Dolma Gurung. I am learning AWS</p>
        <p> This file will be uploaded to Amazon S3 </p>
        </body>
        </html>"""
        newdoc = HtmlDocument(message)
        self.document = newdoc
        print(newdoc)

        
    def save_html_file(self):
        f = open('hello.html','w')
        f.write(self.document.content)
        f.close()


class AWSmanager:
    def __init__(self):
        self.s3 = boto3.resource('s3')

#   #define connections to boto3 and save file to s3
    def save_to_s3(self):  
        s3 = boto3.client('s3') 
        boto3.client('s3').upload_file('hello.html', 'lmtd-class', 'dolma.html')

    def listBucketFile(self, bucketName):
        bucket = self.s3.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

manager = HtmlMananger()
manager.create_html()
manager.save_html_file()

aws = AWSmanager()
aws.save_to_s3()
aws.listBucketFile("lmtd-class")