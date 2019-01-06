import boto3
import os
import pygame
from playsound import playsound
from time import sleep

#Init Pygame to play different soundbits
pygame.mixer.init()

#Start the playback
playsound("Audio/PLAYBACK.mp3", 0)

if __name__ == "__main__":
    #connect to AWS image recognition client
    client = boto3.client('rekognition', 'eu-west-1', aws_access_key_id='???',
                          aws_secret_access_key='???',
                          aws_session_token="???")
    #soundbits files:
    Car = 'Audio/Sound_Car.mp3'
    Nature = 'Audio/Sound_Nature.mp3'
    Sign = 'Audio/Sound_Sign.mp3'

    #Runs forever, if it finds a new image in the folder, it uses the AWS-IR service to scan objects in the photo
    while True:
        sleep(0.5)
        for filename in os.listdir(os.getcwd() + '\\Images'):
            with open(os.getcwd() + "\\Images\\" + filename, 'rb') as image:
                 #create a JSON dict in "response" that holds the objects in the image
                 response = client.detect_labels(Image={'Bytes': image.read()})
            lst = response['Labels']
            results = {}
            #filters and orders the JSON dict so it would only hold the object and the confidence value of that object
            for i in lst:
                results[i['Name']] = i['Confidence']
            if 'Sign' in results:
                if results.get('Sign') > 50:
                    pygame.mixer.music.load(Sign)
                    pygame.mixer.music.play()
                    print("BlaBlaBla...")
            elif 'Nature' in results:
                if results.get('Nature') > 50:
                    pygame.mixer.music.load(Nature)
                    pygame.mixer.music.play()
                    print("Sounds of nature!")
            elif 'Car' in results:
                if results.get('Car') > 50:
                    pygame.mixer.music.load(Car)
                    pygame.mixer.music.play()
                    print("Beep Beep!!!")
            os.remove(os.getcwd() + '/images/' + filename)
            results = {}
            for label in response['Labels']:
                print(label['Name'] + ' : ' + str(label['Confidence']))