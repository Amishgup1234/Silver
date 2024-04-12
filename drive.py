import streamlit as st
import os

# Function to upload file
def upload_file(upload_folder):
    uploaded_file = st.file_uploader("Upload File", type=['txt', 'pdf'])
    if uploaded_file is not None:
        file_path = os.path.join(upload_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        st.success(f"File uploaded successfully: {uploaded_file.name}")

# Function to list and download files
def list_and_download_files(upload_folder):
    st.header("Files in Cloud Drive:")
    files = os.listdir(upload_folder)
    if not files:
        st.write("No files found.")
    else:
        for file in files:
            st.write("- " + file)
            download_button = st.download_button(label="Download", data=open(os.path.join(upload_folder, file), "rb").read(), file_name=file)

def main():
    st.title('Cloud Drive')

    # Create a folder for uploaded files
    upload_folder = "uploaded_files"
    os.makedirs(upload_folder, exist_ok=True)

    # Upload File button at top-right corner
    col_upload = st.sidebar.empty()
    upload_button = col_upload.button("Upload File", key="upload_button")

    if upload_button:
        upload_file(upload_folder)

    # List and Download Files
    list_and_download_files(upload_folder)

if __name__ == "__main__":
    main()
