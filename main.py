import typer
from server import run_development_server, run_server

app = typer.Typer()

@app.command()
def run():
    run_server()


@app.command()
def dev():
    run_development_server()

if __name__ == "__main__":
    app()