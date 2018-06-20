import json
import os

from botocore.vendored import requests


def lambda_handler(event, context):
    post_headers = {
        "Authorization": "Bearer {}".format(os.environ['FB_API_TOKEN']),
    }
    url = "https://graph.facebook.com/{}/feed".format(
        os.environ['FB_GROUP_ID'],
    )

    body = event["body"]
    body = json.loads(body)
    msg = "[**{}**]({})\n**Culprit**\n{}\n**Project**\n{}".format(
        body.get("message"),
        body.get("url"),
        body.get("culprit"),
        body.get("project"),
    )
    
    data = {
        'formatting': 'MARKDOWN',
        'message': msg,
    }
    resp = requests.post(url, headers=post_headers, data=data).json()

    print("Posted to group!")
    return {"statusCode": 200, "body": "Victory!"}
