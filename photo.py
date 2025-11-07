import streamlit as st
import cv2

st.title("📸 Simple Camera Capture with Streamlit + OpenCV")

# Try to open the first available camera
cam = None
for i in range(5):
    temp_cam = cv2.VideoCapture(i)
    if temp_cam.isOpened():
        cam = temp_cam
        break
    temp_cam.release()

if cam is None or not cam.isOpened():
    st.error("Camera not found! Make sure it's connected and not used by another app.")
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
