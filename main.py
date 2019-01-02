import boto3

if __name__ == "__main__":

    imageFile = 'Capture.PNG'
    client = boto3.client('rekognition', aws_session_token="???")

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + imageFile)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')