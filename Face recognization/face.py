import cv2

cap=cv2.VideoCapture(0)
cascade_classifier=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
while True:
	ret,frame=cap.read()
	frame=cv2.cvtColor(frame,0)
	detections=cascade_classifier.detectMultiScale(frame)
	if(len(detections)>1):
		(x,y,w,h)=detections[0]
		frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('frame',frame)
	cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()


