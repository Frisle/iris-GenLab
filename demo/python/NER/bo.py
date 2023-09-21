
from grongier.pex import BusinessOperation

import iris

import os
import datetime


class FileOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)

    def say_hello(self, request:'iris.Ens.StringRequest'):
        self.log_info("Hello "+request.StringValue)

    def on_message(self, request):
        
        title =  text = ""

        if (request.post is not None):
            title = request.post.title                       
            text = request.post.NERtext                       

        line = title
        filename = request.found+".txt"


        self.put_line(filename, line)
        self.put_line(filename, "")
        self.put_line(filename, text)
        self.put_line(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return 

    def put_line(self,filename,string):
        try:
            with open(filename, "a",encoding="utf-8") as outfile:
                outfile.write(string)
        except Exception as e:
            raise e