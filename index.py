#this is a new name: miniature-pancake
from app import (start, App)


app = App()

@app.route('/')
def route_index():
    return app.response.send('Hello, World!')

start(app, __name__)
