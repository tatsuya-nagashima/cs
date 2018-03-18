import cv2

cap = cv2.VideoCapture(0) #Open insight camera
cap.set(3, 640) #width
cap.set(4, 480) #height


while(True):
    ret, frame = cap.read()
    if ret == False:
        break
    else:
        #Display
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Glay scale
        cv2.imshow('capture', frame)

        #If you enter "q", finish capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
