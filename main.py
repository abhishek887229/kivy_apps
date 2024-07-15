import json
from kivy.app import App
import certifi
from kivy.uix.boxlayout import BoxLayout
# this module is used to send asynchronus Request on web server
from kivy.network.urlrequest import UrlRequest


class Interface(BoxLayout):
    #this method will show ffeched data, pass to extra parameters to 
    #so we can get data from api and show here
    def fetched(self,req_body,result):
        polarity=str(round(result[0],2))
        subjectivity=str(round(result[1],2))
        self.ids.label.text=f"polarity : {polarity} and sujectivity: {subjectivity}"
        print(result)

    #send request to api that we created in API folder
    #function to analyze our text
    # on_success verify sucees and return a result
    # req_heeader --> use chartype or language and type of data we want to pass required when using on android
    #certification for security
    def analyzer(self):
        #this sentense is sent to url request in req_body 
        data=json.dumps({"Sentence":self.ids.textinput.text})
        UrlRequest(url="http://127.0.0.1:8000/analysis/",on_success=self.fetched,req_body=data,req_headers={"Content-Type":"application/json; charset=utf-8"},ca_file=certifi.where(),verify=True)
        

#class name will be the name of your app
class Analyzer(App):
    pass


Analyzer().run()