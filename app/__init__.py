from flask import Flask, g
from
from .decorators import json, rate_limit

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from .apis import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    @app.after_request
    def after_request(rv):
        headers = getattr(g, "headers", {})
        rv.headers.extend(headers)
        return rv

    from .auth import auth
    @app.route('/get-auth-token')
    @auth.login_required
    @json
    def get_auth_token():
        return {'token': g.user.generate_auth_token()}

    return app