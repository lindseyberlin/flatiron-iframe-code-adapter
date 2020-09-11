import streamlit as st

def separate_ids(iframe_raw):
    slash_split = iframe_raw.split(sep="/")
    source_id = slash_split[6]
    gid = slash_split[7].split(sep="&")[0].split("=")[1]
    return source_id, gid

def generate_iframe_with_params(iframe_raw,
                                width,
                                height,
                                cell_range):
    source_id, gid = separate_ids(iframe_raw)
    iframe_with_params = f'<iframe style="width: {width}%; height: {height}px;" src="https://docs.google.com/spreadsheets/d/e/{source_id}/pubhtml?gid={gid}&amp;range={cell_range}&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false"></iframe>'
    return iframe_with_params

st.title('Flatiron IFrame Code Adapter')

st.header("Provide your parameters and we'll adjust the raw IFrame code provided by Google Sheets:")

iframe_raw = st.text_input(label="Provide the raw IFrame code copy/pasted from Google Sheets.")

st.write("This code should begin with `<iframe src=` and end with `</iframe>`")

cell_range = st.text_input(label="Provide the cell range", value="A1:B2")

st.write("The cell range should take the form `A1:B2`, where A1 is the top left corner cell and B2 is the bottom right corner cell that you'd like to be displayed.")

width = st.text_input(label="Provide the desired width, as a percent", value=100)

st.write("The width should only include the number, so `100` not `100%`.")

height = st.text_input(label="Provide the desired height, in pixels", value=750)

st.write("The height should only include the number, so `750` not `750px`.")

if st.button("Submit"):
    st.write(iframe_raw, width, height, cell_range)
    test = separate_ids(iframe_raw)
    st.write(test)
    try:
        output = generate_iframe_with_params(iframe_raw, width, height, cell_range)
        st.write(output)
    except:
        st.write("Please check your inputs and try again.")