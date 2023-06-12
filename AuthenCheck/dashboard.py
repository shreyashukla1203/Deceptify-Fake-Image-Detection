import streamlit as st
import plotly.express as px
import util

def app():
    
    st.title("Deceptify")

    st.write(
        "##### Deceptify is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones. For instance, if someone takes your original image and inserts your face into a murder scene or photoshops it onto someone else's body, Deceptify will tag it as fake reducing the chances of it being used to smear you."
    )

    st.write(
        "Simply submit the image, and the machine learning model will evaluate it and provide a response in a fraction of a second"
    )

    st.caption(
        "The application will infer the one label out of 2 labels, as follows: Fake image, Real Image."
    )

    st.info(
        "Try it out now by clicking on Classify Image button"
    )
    

    with st.sidebar:
        st.subheader("💡 Abstract:")

        inspiration = '''
        Deep learning has been successful with GANs, which can be used to create realistic pictures and improve existing ones. However, they can also be used to deceive individuals by generating false data, such as fake faces and synthetic photographs for identification and authentication purposes.
        Advanced picture editing software such as Adobe Photoshop allows for the alteration of complicated input photographs and the creation of high-quality new images. YouTube has step-by-step directions and tutorials for making fictitious graphics, which can be used for defamation, impersonation, and factual distortion. Social media allows fraudulent material to be quickly and extensively shared on the Internet.
        '''

        st.write(inspiration)
        st.markdown("*The dataset was taken from Kaggle and you can find it [here](https://www.kaggle.com/hamzaboulahia/hardfakevsrealfaces).*")

        st.markdown('''The Dataset contains 1288 faces out of which
        <li> 589 are Real </li> 
        <li> 700 are Fake </li>
        ''', unsafe_allow_html=True) 


    if st.button("Classify Image"):
        st.write("Upload a Picture to see if it is a fake or real face.")
        st.markdown('*Need a face to test? Visit this [link]("https://github.com/kanakmi/Deforgify/tree/main/Model%20Training/dataset")*')
        file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
        if file_uploaded is not None:
            res = util.classify_image(file_uploaded)
            c1, buff, c2 = st.columns([2, 0.5, 2])
            c1.image(file_uploaded, use_column_width=True)
            c2.subheader("Classification Result")
            c2.write("The image is classified as **{}**.".format(res['label'].title()))
    


