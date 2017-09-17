# IBM-Watson-Workshop

Hello everyone! Thanks for attending my AI workshop today!

Here are the links I spoke about at the end of the workshop:	

 - [How To Use IBM Watson Visual Recognition AI](https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/?python#introduction)

 - [How IBM Watson AI Works](https://console.bluemix.net/docs/services/visual-recognition/customizing.html#structure)

 - [JSON Explanation](http://www.json.org/)

### Function Documentation:

    classifyURLImage()
**EXPLANATION:** This function prints the information returned from running the classify() method inside our visual_recognition
								object. It prints in json formated form.
								
**VARIABLES** you can change:

 - `exampleURL`: Contains the picture link that will be put through the A.I. to analyze.

**OUTPUT:** a json formatted list of things that the A.I. thinks your picture is. Along with scores to show confidence levels.

    createCustomClassifier()


**EXPLANATION:** This function allows you to create your own custom classifiers. Basically allows you teach the A.I. to recognize something you want it recognize.

**VARIABLES** you can change:   

 - `truckPictures`: Contains the name of the compressed folder full with images that you wish to use to train IBM Watson VisualRecognition positively. (Ex. I used truck pictures to show the A.I. what a truck was.)

   

 - `carPictures`: Contains the name of the compressed folder full with images that you wish to use to show IBM Watson negative examples of what you're trying to define. (Ex. I used car pictures because cars aren't trucks. But they look similar so I wanted Watson to learn differences.)

**OUTPUT:** A status report of what the A.I. is currently at. (Specifically: A.I. id, A.I. name, whether the A.I. is ready or still training.


	checkAllClassifiers() 

**EXPLANATION:** Simply returns a list of classifiers you've made in JSON format.
**VARIABLES** that you can change: 
None
**OUTPUT:** A JSON formatted printed list of all classifiers made by the user.

	deleteClassifier()

**EXPLANATION:** Deletes a specific classifier made by the user.
**VARIABLES** that you can change: 

 - `classID`: a ID unique to a custom made classifier. Input a
   classifier ID and run the deleteClassifier function to delete that
   classifier.

**OUTPUT:** Deletes a given classifier based on recieved ID. 