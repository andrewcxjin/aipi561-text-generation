# Text Generation Service
This mini project is similar to my previous AI Conversational Assistant project where it implements a text generation API using a web interface that connected to Amazon Bedrock. The user can input a prompt and recieve a response from the model (Amazon Titan Text Express V1). AWS permissions have not been granted so the web interface will not actually return a response, but a video demonstration is attached to show what an expected response would look like. 

[Deployed Site](https://wmg2wtcfh4.us-east-1.awsapprunner.com/)

### Usage
The user will input a prompt of their choice via the web interface. The API endpoint will check for the API key (assuming correct permissions have been set up), filter unsafe content, logs the prompt and sends it the AWS model. The current content filter is a simple implementation that checks for inappropriate words. The app will then return the generated response to the user. Security measures are set up through the API key and content filter, while usage metrics are tracked via logs. 

