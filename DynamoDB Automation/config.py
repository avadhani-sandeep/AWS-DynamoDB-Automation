import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sandeep')
    AWS_REGION = 'ap-south-1'
    DYNAMODB_TABLE = 'todo_tasks'
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
    EMAIL = "sbiradar2185@gmail.com"
