from sanic import Sanic
from sanic_ext import render


app = Sanic("Recetario")

# Static file locations
app.static('/static', './static')

# Routes
@app.get("/")
async def hello_world(request):
    return await render("index.jinja")


def run_server():
    app.run(host="0.0.0.0", port=8000, debug=False)

def run_development_server():
    app.run(host="0.0.0.0", port=8000, debug=True)