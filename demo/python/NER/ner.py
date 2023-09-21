from spacy import displacy
import spacy
HTML_WRAPPER = """<div style="NER Detected">{}</div>"""
#funtion used in PEX production BS
def getNER(raw_text):    
    result = ''            
    if len(raw_text.strip()) > 0:
        # Load English tokenizer, tagger, parser and NER
        nlp = spacy.load('en_core_web_sm')
        docx = nlp(raw_text)       
        html = displacy.render(docx, style="ent")
        html = html.replace("\n\n", "\n")
        result = HTML_WRAPPER.format(html)
        return result
    return result    
     
















