import streamlit as st
import cv2
import numpy as np

st.title("📸 Capture Photo with OpenCV + Streamlit")

if st.button("Click your Pic"):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        st.error("Camera not found!")
    else:
        ret, frame = cam.read()
        if ret:
            # Flip image like a mirror
            frame = cv2.flip(frame, 1)
            
            # Save image
            cv2.imwrite("new.png", frame)

            # Convert BGR → RGB for Streamlit display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            st.image(frame, caption="Your Captured Image", use_column_width=True)
        cam.release()
