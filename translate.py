from deep_translator import GoogleTranslator as gt
import streamlit as st

st.title("Translator APP 🌏")
st.subheader("This app translates text from one language to another language")
st.divider()
translator=gt()
lang=translator.get_supported_languages()
text=st.text_area("Enter the text translate",height=150)
col1,col2=st.columns(2)
with col1:
    source_lang=st.selectbox('source lang.',options=lang)
with col2:
    target_lang=st.selectbox('target lang.', options=lang)

if st.button('TRANSLATE'):
    translator = gt(source=source_lang, target=target_lang)
    result = translator.translate(text)

    st.success(f'translated text : {result}')
