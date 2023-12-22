import streamlit as st
import pandas as pd
from io import BytesIO

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def update_excel_sheet(df, num_fields, start_row, end_row):
    for col_num in range(1, num_fields + 1):
        column_letter = chr(ord('A') + col_num - 1)
        st.write(f"Enter values for column {column_letter}:")

        for row_num in range(start_row, end_row + 1):
            content = st.text_input(f"Enter content for {column_letter}{row_num}:", key=f"{column_letter}{row_num}")

            if is_numeric(content):
                df.at[row_num, column_letter] = float(content)
            else:
                df.at[row_num, column_letter] = content

def save_and_open_excel_file(df, file_path):
    try:
        with BytesIO() as content:
            df.to_excel(content, index=False, header=True, engine='openpyxl')
            content.seek(0)

            st.download_button(
                label="Download Excel File",
                data=content,
                key="download_button",
                file_name=f"{file_path}.xlsx",
            )

    except Exception as e:
        st.error(f"Error: {e}")

def create_dynamic_excel_streamlit():
    st.title("Dynamic Excel Streamlit App")

    file_path = st.text_input("Enter the file name (without extension):", value="example_file")
    file_path = f"{file_path}.xlsx"

    num_fields = st.number_input("Enter the number of fields:", min_value=1, step=1, value=3)
    start_row = st.number_input("Enter the start row:", min_value=1, step=1, value=1)
    end_row = st.number_input("Enter the end row:", min_value=start_row, step=1, value=5)

    df = pd.DataFrame(index=range(start_row, end_row + 1), columns=[chr(ord('A') + col) for col in range(num_fields)])

    update_excel_sheet(df, num_fields, start_row, end_row)
    save_and_open_excel_file(df, file_path)

if __name__ == "__main__":
    create_dynamic_excel_streamlit()
