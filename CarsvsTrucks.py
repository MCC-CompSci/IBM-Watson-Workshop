"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
* Author: Alan
* File Name: TrucksVsCars
* Date Created: 9/13/2017
* Last Modified: 9/14/2017
* Python Version: 2.7
""""""""""''"""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                       ALGORITHM
* 1. COMPILE positive and negative pictures of object
* 2. CREATE Watson classifier to recognize positive and
     negative pictures through training
* 3. TEST the classifier 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""MODULES"""
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition


"""VARIABLES"""
exampleURL = "https://tinyurl.com/y7oblnh8" 
carPictures = "cars.zip"
truckPictures = "trucks.zip"
classID = ""


""" OBJECTS """
#Watson Visual Recognition object. Simply call to classify and detect images.
visual_recognition = VisualRecognition('2016-05-20', api_key='b5a4ecc127e8c2ddb36b814b57315c09b9192d20')


class CarsvsTrucks:

    """ FUNCTIONS (NOTE: View README.md for more information on what these functions do)"""

    #Example of pre-classifying images in URL form. 
    #Change the exampleURL variable up above and call this function in order to receive 
    #a report from watson on what it thinks your picture is.
    def classifyURLImage():
        print(json.dumps(visual_recognition.classify(images_url=exampleURL), indent=2))

    #Example of creating a custom classifier.
    #Change the carPictures and the truckPictures variables up above to whatever you have nammed your zip files
    #that contain the images that will be used to train your A.I.. 
    def createCustomClassifier():
        with open(join(dirname(__file__), truckPictures), 'rb') as trucks, \
        open(join(dirname(__file__), carPictures), 'rb') as cars:
            print(json.dumps(visual_recognition.create_classifier('CarsvsTrucks', trucks_positive_examples=trucks, negative_examples=cars), indent=2))

    #Example of checking all classifiers
    #Basically returns a list of classifiers(custom user made A.I.s) in JSON format.
    def checkAllClassifiers():
        print(json.dumps(visual_recognition.list_classifiers(),indent=2))

    #Example of deleting classifiers
    #Basically deletes a classifier(custom made A.I.) based on the give ID in the classID variable.
    def deleteClassifier():
        print(json.dumps(visual_recognition.delete_classifier(classifier_id=classID), indent=2))
        
        

    """CALLING FUNCTIONS. Call your functions here."""

    print("The program is finished!")














    
