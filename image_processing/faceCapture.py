import cv2

cap = cv2.VideoCapture(0) #Open insight camera
cap.set(3, 640) #width
cap.set(4, 480) #height

#Make cascade
cascade_path = "/Users/tatsuya/.pyenv/versions/anaconda3-5.0.1/pkgs/opencv-3.3.1-py36hb620dcb_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)
color = (255,255,255)

cnt = 0
interval = 10 #num of frame
while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    else:
        #Capture face
        if cnt % interval == 0:
            facerect = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        cnt = cnt +1
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=4)

        #Display
        cv2.imshow('capture', frame)

        #If you enter "q", finish capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
