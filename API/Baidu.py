from . import Translate
import urllib
from requests import post
import json
from hashlib import md5

class Baidu(Translate.Translate):
    def customstyles(self):
        return ['color:yellow']
        pass
    
    def translate(self):
        appid='20181116000235418'
        key='0piJC6Iv5AEKysOkhvRD'
        query=self.text.encode('utf-8')
        sign=md5(''.join([appid,self.text,'1',key]).encode()).hexdigest()
  
        JsonRequest={
            'from':'en',
            'to':'zh',
            'q':query,
            'appid':appid,
            'sign':sign,
            'salt':'1'
            }
        JsonResult=post('https://fanyi-api.baidu.com/api/trans/vip/translate',JsonRequest)
        # return JsonResult.json().get('trans_result')[0].get('dst')
        self.resultjson= JsonResult.json()['trans_result']#.get('trans_result',{})
        self.result=self.resultjson
        self.result=','.join([x['dst'] for x in self.result]) if self.result is not None else ''
        return self.result
