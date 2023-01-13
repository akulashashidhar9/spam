import streamlit as st 
import joblib
import base64

# Load the model
spam_clf = joblib.load(open('spamwebappdocker/spam_detector_model.pkl','rb'))

# Load vectorizer
vectorizer = joblib.load(open('spamwebappdocker/vectorizer.pickle', 'rb'))

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true" style='visibility: hidden;'>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )



### MAIN FUNCTION ###
def main(title = "SPAM DETECTION WEB APPLICATION".upper()):
    st.markdown("<h2 style='text-align: center;'>{}</h2>".format(title), 
    unsafe_allow_html=True)
    info = ''
    
    with st.expander("Check if your text is a spam or ham"):
        text_message = st.text_input("Please enter your message")
        if st.button("Predict"):
            prediction = spam_clf.predict(vectorizer.transform([text_message]))

            if(prediction[0] == 0):
                info = 'Great! You are in the safe side the message is Ham'
                st.image("spamwebappdocker/sources/not-spam.webp")
                autoplay_audio("spamwebappdocker/sources/safe.mpeg")

            else:
                info = 'Ohoo no! The message that you entered is Spam'
                st.image("spamwebappdocker/sources/spam.webp")
                autoplay_audio("spamwebappdocker/sources/warning.mpeg")

            st.success('Prediction:{}'.format(info))

if __name__ == "__main__":
    main()