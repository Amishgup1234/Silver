import streamlit as st
import boto3

# Set up AWS S3 client
s3 = boto3.client('s3')

# Streamlit app
st.title("Cloud Storage App")

# File upload
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Upload file to S3
    s3.upload_fileobj(uploaded_file, 'your-bucket-name', uploaded_file.name)
    st.success("File uploaded successfully!")

# File download
file_to_download = st.text_input("Enter filename to download:")
if st.button("Download"):
    try:
        # Download file from S3
        with open(file_to_download, 'wb') as data:
            s3.download_fileobj('your-bucket-name', file_to_download, data)
        st.success("File downloaded successfully!")
    except Exception as e:
        st.error(f"Error downloading file: {e}")
