import cv2
import mediapipe as mp
import pyautogui_templeRun

cap = cv2.VideoCapture(1)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#cap.set(cv2.CAP_PROP_FPS, 15)

fbs = int(cap.get(cv2.CAP_PROP_FPS))

mp_hand = mp.solutions.hands
hands = mp_hand.Hands()     # it has all values in _init_ we need no change

mpdraw = mp.solutions.drawing_utils



finger_coordinates = [(8,6),(12,10),(16,14),(20,18)]
thumbCoordinate = (4,2)


while True:

    st,frame = cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    upcounter = 0
    if results.multi_hand_landmarks:

        listHandPoints = []

        for handLM in results.multi_hand_landmarks:
            for id,lm in enumerate(handLM.landmark):   #id the number of the mark
                # print(id,lm)
                h, w ,c = frame.shape
                x,y = int(lm.x * w),int(lm.y * h)   # for all handmarks in all hands
                #print(id,x,y)
                listHandPoints.append((x,y))
                #cv2.circle(frame,(x,y), 5 , (255,0,0),cv2.FILLED) #draw circle around all hand marks

            mpdraw.draw_landmarks(frame,handLM, mp_hand.HAND_CONNECTIONS)






            for coordinate in finger_coordinates:
                #listHandPoints[coordinate[the 0 element in finger landmark]][y position for that mark]
                if listHandPoints[coordinate[0]][1] < listHandPoints[coordinate[1]][1]:
                    upcounter += 1

            if listHandPoints[thumbCoordinate[0]][0] > listHandPoints[thumbCoordinate[1]][0]:
                upcounter += 1


            pyautogui_templeRun.clicks(upcounter)
            n =""
            if upcounter == 5:
                n = "UP"
            elif upcounter == 4:
                 n = 'Left'
            elif upcounter == 3 | upcounter == 1:
                n ="Down"
            elif upcounter == 2:
                n = 'Right'
            cv2.putText(frame,str(n), (10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3) #draw circle around all hand marks


    cv2.imshow("Handtracking",frame)


    if cv2.waitKey(fbs) & 0xFF == ord('x'):
        break




cap.release()

cv2.destroyAllWindows()
