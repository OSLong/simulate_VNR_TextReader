from pprint import pprint


class Translate():
    def __init__(self,text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text=text


    def beforetranslate(self):
        pass

    def translate(self):
        text=self.text
        pass

    def aftertranslate(self):
        pprint(self.resultjson,indent=4,width=1);
        pass
    
    def customstyles(self):
        return []

    def stylesheet(self):
        default=["font-size:16pt",'color:white']
        default+=self.customstyles()
        return ';'.join(default)

    def result(self):
        self.beforetranslate()
        self.translate()
        self.aftertranslate()
        return self.result

   

