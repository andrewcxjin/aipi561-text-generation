import boto3
import json

def generate_text(prompt):
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 100,
        "temperature": 0.7
    })

    response = bedrock.invoke_model(
        modelId='amazon.titan-text-express-v1', 
        contentType='application/json',
        accept='application/json',
        body=body
    )

    response_body = json.loads(response['body'].read())
    return response_body.get('completion', '[No output]')
