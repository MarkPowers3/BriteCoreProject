from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList
import json

def Alchemy_Encoder():
        _visited_objs = []

        class AlchemyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj.__class__, DeclarativeMeta):
                    # don't re-visit self
                    if obj in _visited_objs:
                        return None

                    _visited_objs.append(obj)

                    fields = {}
                    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                        val = obj.__getattribute__(field)
                        if val is not None:
                            if isinstance(val, InstrumentedList):
                                if len(val) > 0:
                                    fields[field] = val
                            else:
                                fields[field] = val

                    # a json-encodable dict
                    return fields

                return json.JSONEncoder.default(self, obj)

        return AlchemyEncoder