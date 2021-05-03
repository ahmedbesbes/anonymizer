import streamlit as st
import spacy
from annotated_text import annotated_text


@st.cache(suppress_st_warning=True, allow_output_mutation=True, show_spinner=True)
def load_models():
    print("loading models")
    fr_model = spacy.load("./models/fr", disable=["parser", "tagger"])
    en_model = spacy.load("./models/en", disable=["parser", "tagger"])
    models = {"fr": fr_model, "en": en_model}
    return models


def analyze_text(doc, anonymize, selected_entities):

    tokens = []
    for token in doc:
        if (token.ent_type_ == "PERSON") & ("PER" in selected_entities):
            tokens.append((token.text, "Person", "#faa"))
        elif (token.ent_type_ in ["GPE", "LOC"]) & ("LOC" in selected_entities):
            tokens.append((token.text, "Location", "#fda"))
        elif (token.ent_type_ in ["ORG"]) & ("ORG" in selected_entities):
            tokens.append((token.text, "Organization", "#afa"))
        else:
            tokens.append(" " + token.text + " ")

    if anonymize:
        anonymized_tokens = []
        for token in tokens:
            if type(token) == tuple:
                token = ("X" * len(token[0]), token[1], token[2])

            anonymized_tokens.append(token)
        return anonymized_tokens

    else:
        return tokens


models = load_models()

selected_language = st.sidebar.selectbox("Select a language", ("en", "fr"))
selected_model = models[selected_language]
selected_entities = st.sidebar.multiselect(
    "Select entities to detect",
    ["ORG", "PER", "LOC"],
    default=["ORG", "PER", "LOC"],
)

text_container = st.beta_container()
upload_container = st.beta_container()

with text_container:
    input_text = st.text_area("Enter a text to anonymize", height=115)

with upload_container:
    file_uploader = st.file_uploader(
        "Upload a file", type=["txt", "doc", "docx", "pdf"]
    )

doc = selected_model(input_text)
anonymize = st.checkbox("Anonymize")

tokens = analyze_text(doc, anonymize, selected_entities)

annotated_text(*tokens)
