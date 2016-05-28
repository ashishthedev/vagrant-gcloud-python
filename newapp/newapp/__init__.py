import logging

from flask import Flask

def create_app(config, debug=False, testing=False, config_overrides=None):
  app = Flask(__name__)
  app.config.from_object(config)

  app.debug = debug
  app.testing = testing

  if config_overrides:
    app.config.update(config_overrides)

  #Configure logging
  if not app.testing:
    logging.basicConfig(level=logging.INFO)

  #Setup the data model
  with app.app_context():
    model = get_model()
    model.init_app(app)

  from .app import appview
  app.register_blueprint(appview, url_prefix='')

  @app.errorhandler(500)
  def server_error(e):
    return """
    An internal error occurred:<pre>{}</pre>
    """.format(e), 500

  return app

def get_model():
  from . import model_datastore
  model = model_datastore
  return model
