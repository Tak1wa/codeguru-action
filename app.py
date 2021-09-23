import boto3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    client = boto3.client('iam', aws_access_key_id='AAAAAAAAAAAAAAAAAAA', aws_secret_access_key='BBBBBBBBBBBBBBBBBBBBBBBBBb')
    return "Hello, World!!!!!"
