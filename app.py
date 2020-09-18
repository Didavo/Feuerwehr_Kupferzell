from app import create_app
from waitress import serve





print(globals())


app = create_app()
serve(app, host="localhost", port=8000)