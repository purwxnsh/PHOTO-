import streamlit as st
from PIL import Image
import numpy as np

st.title("📸 Capture Photo with Streamlit Camera")

picture = st.camera_input("Click your Pic")

if picture:
    # Convert uploaded image into array
    img = Image.open(picture)
    img_array = np.array(img)

    # Save the image
    img.save("captured_image.png")

    st.image(img_array, caption="✅ Your Captured Image", use_column_width=True)

    st.success("Image saved as captured_image.png")
