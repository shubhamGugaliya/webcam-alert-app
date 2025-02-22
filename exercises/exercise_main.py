import cv2
import streamlit as st
import time

st.title("Motion Detector")
button_1 = st.button("Start camera")
button_2 = st.button("Stop")

print(button_1)

if button_1:
    video = cv2.VideoCapture(0)
    streamlit_image = st.image([])

    while True:
        check, frame = video.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame,text=time.strftime("%A"),org=(20,20),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(20,100,20),thickness=1,lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=time.strftime("%H:%M:%S"), org=(20, 40), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1, color=(20, 100, 20), thickness=1, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)

        if button_2:
            break

