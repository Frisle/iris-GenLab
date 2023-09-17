from genlab import create_app
from genlab.myconfig import *
from flaskext.markdown import Markdown

if __name__ == "__main__":
    # get db info from config file
    database_uri = f'iris://{DB_USER}:{DB_PASS}@{DB_URL}:{DB_PORT}/{DB_NAMESPACE}'
    app = create_app(database_uri)
    Markdown(app)
    app.run('0.0.0.0', port="4040", debug=False)


