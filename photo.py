import streamlit as st
import cv2
import numpy as np

st.title("📸 Click Photo with OpenCV + Streamlit")

# Step 1: Show button to open camera
if 'camera_opened' not in st.session_state:
    st.session_state.camera_opened = False

if st.button("Open Camera"):
    st.session_state.camera_opened = True

# Step 2: Show camera feed only after button click
if st.session_state.camera_opened:
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        st.error("Camera not found!")
    else:
        stframe = st.empty()  # Placeholder for live camera feed
        captured_image = None

        while True:
            ret, frame = cam.read()
            if not ret:
                st.error("Failed to grab frame")
                break

            frame = cv2.flip(frame, 1)  # Mirror image
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            stframe.image(frame_rgb, channels="RGB")

            # Add capture button
            if st.button("Capture Photo"):
                captured_image = frame_rgb
                cv2.imwrite("captured_image.png", cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
                st.success("Photo captured and saved as captured_image.png!")
                break

        cam.release()
