from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # set a secret key, required to render flash messages
    app.config['SECRET_KEY'] = 'dev'

    # loads the config file, required to replace SECRET_KEY in production deployments
    app.config.from_pyfile('config.py', silent=True)
    
    # load the greetings blueprint
    from . import greetings
    app.register_blueprint(greetings.bp)

    # a test endpoint
    @app.route('/test')
    def test_endpoint():
        return 'Okay'
    
    return app
