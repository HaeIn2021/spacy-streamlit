import spacy
from spacy_streamlit import visualize_tokens

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sundar Pichai is the CEO of Google.")
visualize_tokens(doc, attrs=["text", "pos_", "dep_", "ent_type_"])
