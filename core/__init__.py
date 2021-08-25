from flask import Flask

def app_init():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "w92ejoqndoi28ADNAoi2he0"
    from core.public_routes import huffman_translator
    app.register_blueprint(huffman_translator)
    return app