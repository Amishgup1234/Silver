import streamlit as st
import os

# Function to upload file
def upload_file(upload_folder):
    uploaded_file = st.file_uploader("Upload Files", type=['txt', 'pdf'])
    if uploaded_file is not None:
        file_path = os.path.join(upload_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        st.success(f"File uploaded successfully: {uploaded_file.name}")

# Function to list files
def list_files(upload_folder):
    st.header("Files in Cloud Drive:")
    files = os.listdir(upload_folder)
    if not files:
        st.write("No files found.")
    else:
        for file in files:
            st.write("- " + file)

# Function to download file
def download_file(upload_folder):
    file_to_download = st.selectbox("Select a file to download", os.listdir(upload_folder))
    if st.button("Download"):
        file_path = os.path.join(upload_folder, file_to_download)
        with open(file_path, "rb") as f:
            file_content = f.read()
        st.download_button(label="Download File", data=file_content, file_name=file_to_download)

def main():
    st.title('Cloud Drive')

    # Create a folder for uploaded files
    upload_folder = "uploaded_files"
    os.makedirs(upload_folder, exist_ok=True)

    # Sidebar with file actions
    st.sidebar.header("File Actions")
    action = st.sidebar.selectbox("Select Action", ["Upload File", "List Files", "Download File"])

    if action == "Upload File":
        upload_file(upload_folder)
    elif action == "List Files":
        list_files(upload_folder)
    elif action == "Download File":
        download_file(upload_folder)

if __name__ == "__main__":
    main()
