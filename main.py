import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import base64

model = load_model('Model/model.h5')
class_dict = np.load("artifacts/class_names.npy")


def predict(image):
    IMG_SIZE = (1, 224, 224, 3)

    img = image.resize(IMG_SIZE[1:-1])
    img_arr = np.array(img)
    img_arr = img_arr.reshape(IMG_SIZE)

    pred_proba = model.predict(img_arr)
    pred = np.argmax(pred_proba)
    return pred

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

contnt = "<p>Herbal medicines are preferred in both developing and developed countries as an alternative to " \
         "synthetic drugs mainly because of no side effects. Recognition of these plants by human sight will be " \
         "tedious, time-consuming, and inaccurate.</p> " \
         "<p>Applications of image processing and computer vision " \
         "techniques for the identification of the medicinal plants are very crucial as many of them are under " \
         "extinction as per the IUCN records. Hence, the digitization of useful medicinal plants is crucial " \
         "for the conservation of biodiversity.</p>"

if __name__ == '__main__':
    add_bg_from_local("artifacts/Background.jpg")
    new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Medicinal Leaf Classification</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown(contnt, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)

        img = img.resize((300, 300))
        st.image(img)

        if st.button("Predict"):
            pred = predict(img)
            name = class_dict[pred]
            if name == "Alpinia Galanga (Rasna)":
                name = name + "Alpinia Galanga, or Rasna, is traditionally used for its anti-inflammatory properties, aiding in conditions like arthritis, and as a digestive aid to alleviate gastrointestinal discomfort. It also exhibits antimicrobial effects, supporting wound healing and respiratory health."
            elif name == "Amaranthus Viridis (Arive-Dantu)":
                name = name + " Amaranthus viridis, or Arive-Dantu, is utilized medicinally for its potential as an antioxidant and its traditional use in alleviating digestive issues."
            elif name == "Artocarpus Heterophyllus (Jackfruit)":
                name = name + " Artocarpus heterophyllus, or Jackfruit, is valued for its medicinal properties, including its ability to improve digestion and boost immune function."
            elif name == "Azadirachta Indica (Neem)":
                name = name + "Azadirachta indica, or Neem, is renowned for its multifaceted medicinal benefits, notably as an antibacterial and antifungal agent, aiding in skin conditions like acne, and as an antipyretic, helping to reduce fever."
            elif name == "Basella Alba (Basale)":
                name = name + "Basella alba, or Basale, is traditionally utilized for its medicinal properties, notably as a source of antioxidants, supporting overall health, and for its potential as a natural remedy for digestive disorders."
            elif name == "Brassica Juncea (Indian Mustard)":
                name = name + "Brassica juncea, or Indian Mustard, is valued for its medicinal properties, acting as a potent source of antioxidants and exhibiting potential anti-inflammatory effects, beneficial for overall health and wellness."
            elif name == "Carissa Carandas (Karanda)":
                name = name + "Carissa carandas, or Karanda, is esteemed for its medicinal properties, known to alleviate digestive issues like indigestion and constipation, and for its potential as an antimicrobial agent, supporting overall health."
            elif name == "Citrus Limon (Lemon)":
                name = name + "Citrus limon, or Lemon, is prized for its medicinal benefits, notably as a rich source of vitamin C, aiding in immune support and digestion, and for its potential as a natural remedy for respiratory conditions and skin issues."
            elif name == "Ficus Auriculata (Roxburgh fig)":
                name = name + "Ficus auriculata, or Roxburgh fig, is utilized medicinally for its potential as an anti-inflammatory and analgesic agent, known to alleviate pain and swelling, and for its traditional use in treating gastrointestinal disorders like diarrhea and dysentery."
            elif name == "Ficus Religiosa (Peepal Tree)":
                name = name + " Ficus religiosa, or Peepal Tree, holds medicinal significance for its anti-inflammatory properties, aiding in conditions like arthritis, and its traditional use in managing respiratory ailments such as asthma and bronchitis."
            elif name == "Hibiscus Rosa-sinensis":
                name = name + "Hibiscus rosa-sinensis is valued medicinally for its potential to lower blood pressure and cholesterol levels, and for its traditional use in promoting hair growth and enhancing skin health due to its antioxidant-rich properties."
            elif name == "Jasminum (Jasmine)":
                name = name + "Jasminum, or Jasmine, is utilized medicinally for its calming properties, aiding in stress reduction and promoting relaxation, and for its traditional use in relieving headaches and anxiety symptoms."
            elif name == "Mangifera Indica (Mango)":
                name = name + "Mangifera indica, or Mango, is valued for its medicinal properties, serving as a rich source of vitamins, antioxidants, and enzymes, which support immune function and aid in digestion, while also exhibiting potential anti-inflammatory effects beneficial for overall health."
            elif name == "Mentha (Mint)":
                name = name + "Mentha, or Mint, is esteemed for its medicinal properties, known for its ability to soothe digestive discomfort, alleviate nausea, and promote respiratory health due to its menthol content, making it a popular choice for herbal remedies."
            elif name == "Moringa Oleifera (Drumstick)":
                name = name + "Moringa oleifera, or Drumstick, is renowned for its medicinal properties, serving as a potent source of nutrients and antioxidants, aiding in immune support, and exhibiting potential anti-inflammatory effects, contributing to overall health and wellness."
            elif name == "Muntingia Calabura (Jamaica Cherry-Gasagase)":
                name = name + "Muntingia calabura, or Jamaica Cherry-Gasagase, is utilized medicinally for its potential as an anti-inflammatory and antimicrobial agent, aiding in wound healing and immune support, while also showing promise in managing gastrointestinal disorders like diarrhea and dysentery."
            elif name == "Murraya Koenigii (Curry)":
                name = name + "Murraya koenigii, or Curry Leaf, is valued medicinally for its potential to regulate blood sugar levels and aid in digestion, while also exhibiting antioxidant properties that support overall health and wellness."
            elif name == "Nerium Oleander (Oleander)":
                name = name + "Nerium oleander, or Oleander, has limited medicinal use due to its extreme toxicity; however, some traditional practices employ it cautiously for conditions like heart failure and malaria, as its compounds may have potential therapeutic effects when properly processed and administered under strict medical supervision."
            elif name == "Nyctanthes Arbor-tristis (Parijata)":
                name = name + "Nyctanthes arbor-tristis, or Parijata, is esteemed in traditional medicine for its anti-inflammatory and analgesic properties, often used to alleviate pain associated with arthritis and to treat respiratory conditions like asthma, while also showing potential in managing fever and promoting overall wellness."
            elif name == "Ocimum Tenuiflorum (Tulsi)":
                name = name + "Ocimum tenuiflorum, or Tulsi, is revered in Ayurveda for its diverse medicinal properties, acting as an adaptogen to combat stress, boost immunity, and aid in respiratory health, while also exhibiting antimicrobial effects, supporting overall wellness."
            elif name == "Piper Betle (Betel)":
                name = name + "Piper betle, or Betel Leaf, is valued medicinally for its potential to aid digestion, reduce inflammation, and exhibit antimicrobial properties, often used in traditional medicine practices for oral hygiene, respiratory health, and wound healing."
            elif name == "Plectranthus Amboinicus (Mexican Mint)":
                name = name + "Plectranthus amboinicus, or Mexican Mint, is esteemed for its medicinal properties, known to aid digestion and alleviate respiratory issues, while also exhibiting antimicrobial effects that support overall health and wellness."
            elif name == "Pongamia Pinnata (Indian Beech)":
                name = name + "Pongamia pinnata, or Indian Beech, is valued medicinally for its potential as an anti-inflammatory and analgesic agent, often used to alleviate pain and inflammation associated with various conditions, while also showing promise in treating skin disorders due to its antimicrobial properties."
            elif name == "Psidium Guajava (Guava)":
                name = name + "Psidium guajava, or Guava, is esteemed for its medicinal properties, serving as a rich source of vitamin C and antioxidants, aiding in immune support and digestion, while also exhibiting potential anti-inflammatory effects, beneficial for overall health and wellness."
            elif name == "Punica Granatum (Pomegranate)":
                name = name + "Punica granatum, or Pomegranate, is prized for its medicinal benefits, serving as a potent source of antioxidants and phytochemicals that support heart health, aid digestion, and may help reduce inflammation, contributing to overall well-being."
            elif name == "Santalum Album (Sandalwood)":
                name = name + "Santalum album, or Sandalwood, is esteemed in traditional medicine for its anti-inflammatory and antimicrobial properties, used to soothe skin irritations and treat conditions like acne, while also promoting relaxation and mental clarity through its aromatic qualities."
            elif name == "Syzygium Cumini (Jamun)":
                name = name + "Syzygium cumini, or Jamun, is valued medicinally for its potential to regulate blood sugar levels, aid in digestion, and exhibit antioxidant properties, offering support for overall health and diabetes management."
            elif name == "Syzygium Jambos (Rose Apple)":
                name = name + "Syzygium jambos, or Rose Apple, is utilized medicinally for its potential to aid in digestion and improve oral health due to its antimicrobial properties, while also providing essential nutrients and antioxidants that support overall wellness."
            elif name == "Tabernaemontana Divaricata (Crape Jasmine)":
                name = name + "Tabernaemontana divaricata, or Crape Jasmine, is valued in traditional medicine for its potential as an antipyretic and analgesic, often used to alleviate fever and pain, while also showing promise in treating skin disorders due to its anti-inflammatory properties."
            else : name == "Trigonella Foenum-graecum (Fenugreek)"
            name = name + "Trigonella foenum-graecum, or Fenugreek, is esteemed for its medicinal properties, known to regulate blood sugar levels and aid digestion, while also exhibiting potential benefits for lactation support and promoting skin health."







            result = '<p style="font-family:sans-serif; color:White; font-size: 16px;">The given image ' \
                        'is '+name+'</p>'
            st.markdown(result, unsafe_allow_html=True)




