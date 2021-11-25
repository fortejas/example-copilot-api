import os
from fastapi import FastAPI

app = FastAPI()


CONFIG_VAR = os.environ.get('CONFIG_VAR')
SECRET_VAR = os.environ.get('SECRET_VAR')


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/health')
def read_health():
    return {'status': 'ok'}


@app.get('/config')
def read_config():
    return {
        'config_var': CONFIG_VAR,
        'secret_var': SECRET_VAR
    }
