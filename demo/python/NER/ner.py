from spacy import displacy
import spacy
import re,os
#funtion used in PEX production BS
def getNER(raw_text):    
    result = ''            
    if len(raw_text.strip()) > 0:
        # Load English tokenizer, tagger, parser and NER
        nlp = spacy.load('en_core_web_sm')        
        docx = nlp(raw_text)                      
        pattern = re.compile('<.*?>')
        html = displacy.render(docx, style="ent")
        html = html.replace("\n\n", "\n")        
        result = re.sub(pattern, '', html).strip()
        without_empty_lines = os.linesep.join(
           [
                line for line in result.splitlines()
                if line
            ]
        )        
        return without_empty_lines
    return result    
     
















