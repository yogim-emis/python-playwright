import json


class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)


USERS = DictObject.from_dict({
    'default': {
		'usertype': 'Adminuser',
        'username': 'yogim-emis',
        'password': '#3misHealth',
		'secret': 'QQBM6LDK6MES5H4UKXGD6BOA43C4ZNFCPZQB2PL5H5EY2CVUCGAA'
    },
    'int': {
		'usertype': 'Adminuser',
        'username': 'yogim-emis',
        'password': '#3misHealth',
		'secret': 'QQBM6LDK6MES5H4UKXGD6BOA43C4ZNFCPZQB2PL5H5EY2CVUCGAA'
    },
    'staging': {
		'usertype': 'Adminuser',
        'username': 'yogim-emis',
        'password': '#3misHealth',
		'secret': 'SBMIL4XPHDPOQLIRQJP5GSXRYHWP36R2JMV7IULBFLHI5DK6RBVQ'
    },      
    'emisxint': {
		'usertype': 'GPuser',
        'username': 'EXAPathwayTesting@emishealth.com',
        'password': 'lcTjpO%L@Z176Q!UEhnL7',
		'secret': 'pv3u37wxe7njvqdj'
    },
    'emisxstaging': {
		'usertype': 'GPuser',
        'username': 'EXAPathwayTesting@emishealth.com',
        'password': 'Lv4ic>]ujHra,N7Vgvlf=b',
		'secret': 'oerl33iyfhtsoqw4v'
    }
})
