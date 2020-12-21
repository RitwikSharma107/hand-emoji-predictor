import streamlit as st 

def main():

    html1 = """
        <div style="background-color:#0562f7;border-radius:10px;border-style:solid;border-color:black;padding:10px">
        <h2 style="color:white;text-align:center;">Hand Emoji Predictor</h2>
        </div>
        """
    st.markdown(html1,unsafe_allow_html=True)
    st.write('')
    st.sidebar.title('Machine Learning Project')
    nav = st.sidebar.radio('',['Home','About',"Technologies Used","Reference"])
    if nav == 'Home':
        video = open('Hand_Emoji_Preds.mp4','rb').read()
        st.video(video)
        
    if nav == 'About':
        st.subheader('This project is used to predict emojis from hand gestures using webcam.') 
        st.subheader('It requires webcam in order to capture, store and evaluate the hand gestures.') 
        st.subheader('It can be divided into four parts:- ')
        html2 = """
        <div>
        <ol style="font-weight: bold;">
            <li>The first part includes generation of hand gesture dataset from webcam.</li>
            <li>The second part converts hand gesture dataset into CSV file.</li>
            <li>The third part involves generation and evaluation of deep learning model using keras and tensorflow as backend.</li>
            <li>The fourth part involves application of the model in real time. </li>
        </ol>
        </div>
        """
        st.markdown(html2,unsafe_allow_html=True)

    if nav == 'Technologies Used':
        st.write('')
        st.header("Technologies Used")
        html3 = """
        <div>
        <ul>
            <li>Python</li>
            <li>TensorFlow </li>
            <li>Keras </li>
            <li>OpenCV</li>
            <li>Jupyter Notebook</li>
        </ul>
        </div>
        """
        st.markdown(html3,unsafe_allow_html=True)

    if nav == 'Reference':
        st.subheader('I want to thank Mr. Akshay Bahadur whose project (Emojinator) inspired me to make this project.')
        st.write('')
        st.info('You can view the referred project by clicking the below link')
        html4 = """
        <div>
        <a href="https://github.com/akshaybahadur21/Emojinator">Emojinator Project</a>
        </div>
        """
        st.markdown(html4,unsafe_allow_html=True)

    st.sidebar.header('Developed by')
    html_string = "<div><a href='https://ritwiksharma107.github.io/portfolio/' style='color:#e60067; text-decoration:none;'>Ritwik Sharma</a></div>"
    st.sidebar.markdown(html_string, unsafe_allow_html=True)

    page_bg_img = '''
    <style>
    body {
    background-image: url("https://wallpaperaccess.com/full/3898677.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
