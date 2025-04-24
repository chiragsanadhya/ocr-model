import streamlit as st
import requests
from PIL import Image
import io
import json

# Configure page settings
st.set_page_config(
    page_title="Multi-Modal OCR",
    page_icon="📝",
    layout="wide"
)

def main():
    st.title("Multi-Modal OCR System")
    st.write("Upload an image to extract text from both printed and handwritten content")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display the uploaded image
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)

        # Process button
        if st.button("Extract Text"):
            with st.spinner("Processing image..."):
                try:
                    # Prepare the file for the API request
                    files = {"file": uploaded_file.getvalue()}
                    
                    # Make API request
                    response = requests.post(
                        "http://localhost:8000/ocr/process",
                        files=files
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        with col2:
                            st.subheader("Extracted Text")
                            
                            # Display results in a nice format
                            for detection in result["detections"]:
                                with st.expander(f"Text ({detection['text_type']})"):
                                    st.write(f"**Text:** {detection['text']}")
                                    st.write(f"**Confidence:** {detection['confidence']:.2%}")
                                    st.write("**Location:**")
                                    st.write(f"- X: {detection['bounding_box']['x']}")
                                    st.write(f"- Y: {detection['bounding_box']['y']}")
                                    st.write(f"- Width: {detection['bounding_box']['width']}")
                                    st.write(f"- Height: {detection['bounding_box']['height']}")
                            
                            st.success(f"Processing Time: {result['processing_time']:.2f} seconds")
                    else:
                        st.error("Error processing the image")
                        
                except Exception as e:
                    st.error(f"Error connecting to the API: {str(e)}")

    # Add information about supported features
    with st.sidebar:
        st.header("Features")
        st.write("- Printed Text Detection")
        st.write("- Handwritten Text Detection")
        st.write("- Multi-language Support")
        
        st.header("Supported Formats")
        st.write("- PNG")
        st.write("- JPEG/JPG")

if __name__ == "__main__":
    main()