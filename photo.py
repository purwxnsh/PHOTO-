import streamlit as st
import cv2

st.title("📸 Simple Camera Capture with Streamlit + OpenCV")

# Replace 0 with the camera index that works on your system
camera_index = 0
cam = cv2.VideoCapture(camera_index)

if not cam.isOpened():
    st.error("Camera not found! Make sure it's connected, not used by another app, and permissions are granted.")
else:
    st.info("Camera is ON! Press 'Capture Photo' to take a picture.")
    stframe = st.empty()  # Placeholder for live feed
    captured = False

    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)  # Mirror effect
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB")

        # Capture photo when button is pressed
        if st.button("Capture Photo") and not captured:
            cv2.imwrite("captured_image.png", cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
            st.success("Photo captured and saved as captured_image.png!")
            captured = True
            break

    cam.release()

