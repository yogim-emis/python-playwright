import json


class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)


PATHWAYTESTDATA = DictObject.from_dict({
    'scenario_001': {
		'sql': 'SELECT registration_id,nhs_no,patient_id,age,patient_name,postcode,riskcategory,confidentiality_policy_id,organisation FROM (VALUES (\'081295BF-3D65-4969-B542-3AC8749248B4\', \'4514937711\', 10084, 10084, 69, \'POOLE, Victoria (Mrs)\', \'HO19 1UO\', \'Born in higher prevelence countries or travels widely,Transfusion\', -1, \'CDB-50002\'), (\'1175C8DE-941E-4F26-A54C-0F825DF6FD42\', \'4169517857\', 12158, 12158, 42, \'SWIFT, Anne (Ms)\', \'SG2 9PC\', \'Serum ALT level,HIV or HIV risk related codes,Contaminated blood\', -1, \'CDB-50002\'), (\'16917801-6C73-4ECC-A0F9-4C1377CB3351\', \'9615583529\', 12133, 12133, 47, \'MORTON, Lee (Mr)\', \'CF18 7YZ\', \'hepatitis B infection,HIV or HIV risk related codes,Organ transplant,Serum ALT level\', -1, \'CDB-50002\'), (\'017D757A-5A00-45F4-8A03-1C666252EA69\', \'5559927678\', 13849, 13849, 59, \'ROBERTSON, Angela (Mrs)\', \'ZG16 14BC\', \'Serum ALT level,Homeless,Liver disease\', -1, \'CDB-50003\'), (\'085192AA-7AA1-4A5D-A93D-04CDD02A82FF\', \'5218580244\', 10070, 10070, 75, \'WHITTAKER, Adam (Mr)\', \'HM2 17YV\', \'Liver disease,HIV or HIV risk related codes,Transfusion\', -1, \'CDB-50002\')) AS mock_table(registration_id,nhs_no,patientid,patient_id,age,patient_name,postcode,riskcategory,confidentiality_policy_id,organisation)',
        'colmap': '{"registration_id": "Registration ID", "nhs_no": "NHS Number", "patient_id": "Patient ID", "patient_name": "Name", "postcode": "Postcode", "riskcategory": "All Risks", "organisation": "GP CDB", "_coalesce_patient": "patient_name"}',
        'wordingtandc' : 'This is a test pathway.\n No terms and conditions are applicable.',
        'wordinggpsharing' : 'No restriction on use of shared data.',
        'dsgname': 'Test Data Sharing Group for only one organisation',
        'dsgorganisationids': '50002',
        'dsgdisplayname': 'DSG is for 50002 only'
    }
})
