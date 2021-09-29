from flask import Flask
from flask import request, jsonify
import boto3

app = Flask(__name__)

smr = boto3.client('sagemaker-runtime')


@app.route('/pred', methods=['POST'])
def predict():
    # make prediction on sagemaker endpoint
    body = request.get_json()
    # print(type(body))
    # print(body)
    data = body['data']
    r = smr.invoke_endpoint(EndpointName='MyEndPoint', Body=data, ContentType='text/csv')
    prediction = r['Body'].read().decode('utf-8')
    print(prediction)
    response = {'prediction': prediction}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
