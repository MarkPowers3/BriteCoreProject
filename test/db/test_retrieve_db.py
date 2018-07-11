from orm.base import Session
from orm.risk import Risk
import json
from util.alchemy_encoder import Alchemy_Encoder


session = Session()

# 3 - extract all risk
risks = session.query(Risk).all()
#risk = session.query(Risk).get(2)

# 4 - print risk details
print('\n### All risks:')
for risk in risks:
    print(f'id: {risk.id}, name: {risk.name}, lob: {risk.lob}')

    for field in risk.fields:
        print(f'\t id: {field.id}, uniqueId: {field.uniqueId}, name: {field.name}, type: {field.type}, maxlength: {field.maxLength}, ')

        for option in field.options:
            print(f'\t\t id: {option.id}, val: {option.val}, text: {option.text} ')

    print('\n')

s = json.dumps(risks[0], cls=Alchemy_Encoder(), check_circular=False)
print(f'risk: {s}')

