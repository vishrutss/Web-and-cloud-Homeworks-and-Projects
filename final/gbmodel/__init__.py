model_backend = 'datastore'

if model_backend == 'datastore':
    from .model_datastore import model
elif model_backend == 'sqlite3':
    from .model_sqlite3 import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel

