import json


class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)


AUT = DictObject.from_dict({
    'int': {
		'weburl': 'https://www-test.testemisnightingale.co.uk/',
        'authorurl': 'https://author.emispathway.dev.emishealthsolutions.com/',
        'coordinatorurl': 'https://coordinator.emispathway.dev.emishealthsolutions.com/'
    },
	'staging': {
		'weburl': 'https://www.stagingemisinsights.co.uk/',
        'authorurl': 'https://author.emispathway.stg.emis-x.uk/',
        'coordinatorurl': 'https://coordinator.emispathway.stg.emis-x.uk/'        
	},
    'emisx_gp_int': {
        'weburl': 'https://host.int.emishealthsolutions.com/?emisweb=false'
    },
    'emisx_gp_staging': {
        'weburl': 'https://host.stg.emis-x.uk/?emisweb=false'
    }

})
