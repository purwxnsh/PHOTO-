import streamlit as st
import cv2
import numpy as np

st.title("📸 Robust Camera Capture with Streamlit + OpenCV")

# Initialize session state
if 'camera_opened' not in st.session_state:
    st.session_state.camera_opened = False

if st.button("Open Camera"):
    st.session_state.camera_opened = True

if st.session_state.camera_opened:
    # Automatically find the first available camera
    cam = None
    for i in range(5):  # Check indexes 0-4
        test_cam = cv2.VideoCapture(i)
        if test_cam.isOpened():
            cam = test_cam
            break
        test_cam.release()

    if cam is None or not cam.isOpened():
        st.error("Camera not found! Make sure it's connected, not used by another app, and you have given permission.")
    else:
        st.info("Camera opened! Press 'Capture Photo' to take a picture.")
        stframe = st.empty()  # Placeholder for live camera feed
        captured = False

        while True:
            ret, frame = cam.read()
            if not ret:
                st.error("Failed to grab frame.")
                break

            # Mirror image like a selfie camera
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame_rgb, channels="RGB")

            # Capture button
            if st.button("Capture Photo") and not captured:
                cv2.imwrite("captured_image.png", cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
                st.success("Photo captured and saved as captured_image.png!")
                captured = True
                break

        cam.release()
