import boto3
import json
import picamera
import time
import sys


class Scanner:
    def __init__(self, URL=0):
        self.Frame = []
        self.status = False
        self.isstop = False

        self.capture = picamera.PiCamera()
        time.sleep(2)
        self.start()

    def start(self):
        print("ipcom started!!")

    def stop(self):
        self.isstop = True
        print("ipcom stopped!!")

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def get_photo(self, filename):
        self.capture.capture(filename)

def detect(photo):
    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])
    # response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        # print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
        #       + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        awake = faceDetail['EyesOpen']['Value']
        print(str(awake))
        # print('Here are the other attributes:')
        # print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return awake


if __name__ == "__main__":
    
    s = Scanner()
    newphoto = 'photos/photo_face.png'
    s.get_photo(newphoto)

    photos = ['photos/openeye.jpg',
            'photos/sleepy.jpg']
    photos.append(newphoto)

    for i in range(len(photos)):
        print(str(i) + ' photo should be' + photos[i])
        photo = photos[i]
        isawake = detect(photo)

        



