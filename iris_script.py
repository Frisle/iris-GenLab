import iris
from transformers import pipeline
#from iris import ipm
#assert ipm('load /home/irisowner/dev -v')

# switch namespace to the %SYS namespace
iris.system.Process.SetNamespace("%SYS")

# set credentials to not expire
iris.cls('Security.Users').UnExpireUserPasswords("*")

# switch namespace to IRISAPP built by merge.cpf
iris.system.Process.SetNamespace("IRISAPP")

import spacy.cli
import nltk
spacy.cli.download("en_core_web_sm")
nltk.download('punkt')

#init Sentimental analysis pipeline
classifier = pipeline('sentiment-analysis')  
#init GPT2 text generation model
classifier = pipeline('text-generation', model = 'gpt2')
   
# load ipm package listed in module.xml
iris.cls('%ZPM.PackageManager').Shell("load /home/irisowner/dev -v")




