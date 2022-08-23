"""Application entry point."""
from flask_code import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True,port=5000)
