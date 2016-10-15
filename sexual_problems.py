import operator

result = [{u'faceRectangle': {u'width': 220, u'top': 124, u'left': 319, u'height': 220}, u'scores': {u'sadness': 2.405169e-06, u'neutral': 0.004737595, u'contempt': 3.80436541e-05, u'disgust': 1.12454254e-05, u'anger': 2.84782072e-06, u'surprise': 4.09142376e-06, u'fear': 3.45566669e-08, u'happiness': 0.995203733}}, {u'faceRectangle': {u'width': 153, u'top': 226, u'left': 25, u'height': 153}, u'scores': {u'sadness': 0.0006249004, u'neutral': 0.9822587, u'contempt': 0.0138994809, u'disgust': 7.737188e-06, u'anger': 2.87497733e-05, u'surprise': 7.097867e-05, u'fear': 4.812748e-07, u'happiness': 0.00310896849}}]
result2=[{u'faceId': u'74559527-cfd2-4a5b-b6ce-91fb0d116fd6', u'faceRectangle': {u'width': 220, u'top': 124, u'height': 220, u'left': 319}, u'faceAttributes': {u'gender': u'male', u'age': 28.8}}, {u'faceId': u'7a737fd7-7318-4896-8ae2-e888fa33333c', u'faceRectangle': {u'width': 153, u'top': 226, u'height': 153, u'left': 25}, u'faceAttributes': {u'gender': u'male', u'age': 28.1}}]

for currFace in range(len(result)):
	result1_Face = result[currFace]
	faceRectangle = result1_Face['faceRectangle']
	currEmotion = max(result1_Face['scores'].items(), key=operator.itemgetter(1))[0]
	result2_face = result2[currFace]
	age = result2_face['faceAttributes']['age']
	gender = result2_face['faceAttributes']['gender']

print(currEmotion)