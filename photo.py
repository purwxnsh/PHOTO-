import streamlit as st
import cv2

st.title("📸 Capture Photo with OpenCV + Streamlit")

if st.button("Click your Pic"):
    cam = None
    # Try multiple camera indexes to find a working one
    for i in range(5):
        temp_cam = cv2.VideoCapture(i)
        if temp_cam.isOpened():
            cam = temp_cam
            break
        temp_cam.release()

    if cam is None or not cam.isOpened():
        st.error("Camera not found! Make sure it's connected, not used by another app, and permissions are granted.")
    else:
        ret, frame = cam.read()
        if ret:
            frame = cv2.flip(frame, 1)  # Mirror effect
            cv2.imwrite("captured_image.png", frame)  # Save the image
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert for Streamlit
            st.image(frame_rgb, caption="Your Captured Image", use_column_width=True)
        else:
            st.error("Failed to grab frame from camera.")
        cam.release()
