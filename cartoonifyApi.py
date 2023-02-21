import requests
import io
import streamlit as st

st.set_page_config(page_title='Cartoon Yourself')

st.title('Cartoon Yourself')

uploaded_file = st.file_uploader('Choose an image file', type=['jpg',
                                 'jpeg', 'png'])

cartoon_styles = [
    'pixar',
    'pixar_plus',
    '3d_cartoon',
    'angel',
    'angel_plus',
    'demon',
    'ukiyoe_cartoon',
    'amcartoon',
    'bopu_cartoon',
    'jpcartoon_head',
    'jpcartoon',
    'anime',
    'hkcartoon',
    'classic_cartoon',
    'tccartoon',
    'handdrawn',
    'sketch',
    'artstyle',
    ]

selected_style = st.selectbox('Select a cartoon style', cartoon_styles)

if st.button('Submit'):

    # Create the multipart/form-data payload

    payload = {'image': ('filename', io.BytesIO(uploaded_file.read()),
               'image/jpeg'), 'type': (None, selected_style)}

    # Set the headers for the request

    headers = \
        {'X-RapidAPI-Key': 'b99eb2b9bamsh6ea17b1a23163d6p116928jsn2b8639bd410f',
         'X-RapidAPI-Host': 'cartoon-yourself.p.rapidapi.com'}

    # Make the request using requests.post() and pass the payload and headers

    response = \
        requests.post('https://cartoon-yourself.p.rapidapi.com/facebody/api/portrait-animation/portrait-animation'
                      , files=payload, headers=headers)

    # Convert the response to a dictionary

    response_dict = response.json()
    print ('\nresponse_dict :- ', response_dict, '\n')

    # Replace backslashes in the image URL with nothing

    image_url = response_dict['data']['image_url'].replace('\\', '')

    (col1, col2) = st.columns(2)
    with col1:
        st.subheader('Original Image')
        st.image(uploaded_file, use_column_width=True)
    with col2:
        st.subheader('Cartoonified Image')
        st.image(image_url, use_column_width=True)
