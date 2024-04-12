import streamlit as st
import boto3
import os

# Function to upload file to S3
def upload_to_s3(file, bucket_name, folder_path=''):
    s3 = boto3.client('s3')
    s3.upload_fileobj(file, bucket_name, os.path.join(folder_path, file.name))

# Function to download file from S3
def download_from_s3(file_key, bucket_name):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    return obj['Body'].read()

# Function to list files in a folder in S3
def list_files_in_folder(bucket_name, folder_path=''):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)
    files = []
    for obj in response.get('Contents', []):
        files.append(obj['Key'])
    return files

# Function to create a folder in S3
def create_folder_in_s3(folder_name, bucket_name):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=(folder_name + '/'))

# Streamlit app code
def main():
    st.title('Cloud Drive')

    st.sidebar.header("File Actions")
    action = st.sidebar.selectbox("Select Action", ["List Files", "Upload File", "Create Folder"])

    bucket_name = "your-bucket-name"
    folder_path = "user_files"  # Change this to your desired folder structure

    if action == "List Files":
        st.header("Files in Cloud Drive:")
        files = list_files_in_folder(bucket_name, folder_path)
        if len(files) == 0:
            st.write("No files found.")
        else:
            for file in files:
                st.write("- " + file)

    elif action == "Upload File":
        st.header("Upload File to Cloud Drive:")
        uploaded_file = st.file_uploader("Choose a file to upload", type=['txt', 'pdf'])
        if uploaded_file is not None:
            upload_to_s3(uploaded_file, bucket_name, folder_path)
            st.success("File uploaded successfully!")

    elif action == "Create Folder":
        st.header("Create Folder in Cloud Drive:")
        folder_name = st.text_input("Enter folder name:")
        if st.button("Create Folder") and folder_name:
            create_folder_in_s3(folder_name, bucket_name)
            st.success(f"Folder '{folder_name}' created successfully!")

if __name__ == "__main__":
    main()
