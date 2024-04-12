import streamlit as st
import boto3

# Function to upload file to S3
def upload_to_s3(file, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_fileobj(file, bucket_name, file.name)

# Function to download file from S3
def download_from_s3(file_key, bucket_name):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    return obj['Body'].read()

# Streamlit app code
def main():
    st.title('Cloud Drive')

    uploaded_file = st.file_uploader("Upload Files", type=['txt', 'pdf'])
    if uploaded_file is not None:
        st.write("File Uploaded Successfully!")
        upload_to_s3(uploaded_file, "your-bucket-name")

    file_key = st.text_input("Enter File Key:")
    if st.button("Download"):
        if file_key:
            file_contents = download_from_s3(file_key, "your-bucket-name")
            st.write("File Downloaded Successfully!")
            st.write(file_contents.decode('utf-8'))

if __name__ == "__main__":
    main()
