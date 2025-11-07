import streamlit as st
import cv2
import numpy as np

st.title("📸 Click Photo with OpenCV + Streamlit")

# Initialize session state
if 'camera_opened' not in st.session_state:
    st.session_state.camera_opened = False

# Step 1: Show button to open camera
if st.button("Open Camera"):
    st.session_state.camera_opened = True

# Step 2: Show camera feed only after button click
if st.session_state.camera_opened:
    # Try multiple camera indexes in case 0 fails
    cam = None
    for i in range(3):  # Try 0,1,2
        cam_test = cv2.VideoCapture(i)
        if cam_test.isOpened():
            cam = cam_test
            break
        cam_test.release()

    if cam is None or not cam.isOpened():
        st.error("Camera not found! Make sure it's connected and not used by another app.")
    else:
        stframe = st.empty()  # Placeholder for live camera feed
        captured_image = None

        st.info("Press 'Capture Photo' to take a picture")

        while True:
            ret, frame = cam.read()
            if not ret:
                st.error("Failed to grab frame")
                break

            frame = cv2.flip(frame, 1)  # Mirror effect
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame_rgb, channels="RGB")

            # Capture button
            if st.button("Capture Photo"):
                captured_image = frame_rgb
                cv2.imwrite("captured_image.png", cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
                st.success("Photo captured and saved as captured_image.png!")
                break

        cam.release()
