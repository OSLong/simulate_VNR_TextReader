from . import Translate

from urllib import request, parse
from json import loads
 

class Youdao(Translate.Translate):
    def customstyles(self):
        return ['color:blue']
        pass
    
    def translate(self):
        text=self.text
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        data = {
            'i': text,
            'from': 'jp',
            'to': 'zh',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '1530587957768',
            'sign': 'b44bb25b9e94bbd6973bb0d501e81fcd',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }
        # 参数data需要的说是bytes格式
        data = parse.urlencode(data).encode()
        header = {
            'Accept': 'application / json, text / javascript, * / *; q = 0.01',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Connection': 'keep - alive',
            'Content - Length': '203',
            'Content - Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1977936130@10.168.8.63; JSESSIONID=aaawJR8e1J4Seh0JNjErw; OUTFOX_SEARCH_USER_ID_NCOO=2054766981.1307113; fanyi-ad-id=46607; fanyi-ad-closed=1; ___rl__test__cookies=1530587957758',
            'Host': 'fanyi.youdao.com',
            'Origin': ' http: // fanyi.youdao.com',
            'Referer': 'http: // fanyi.youdao.com /',
            'User - Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'X- Requested - With': ' XMLHttpRequest'
        }
        req = request.Request(url=url, data=data, headers=header)
      
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        result = loads(html)
        self.resultjson=result
        self.result=result['translateResult']
        self.result=','.join(x[0]['tgt'] for x in self.result)
        