from flask import Flask
from .controllers.downloads_controller import DownloadsController
from .controllers.search_controller import SearchController


app = Flask(__name__)
app.url_map.strict_slashes = False

controller_pairs = [
    ('/search', SearchController),
    ('/download', DownloadsController),
]

for route, klass in controller_pairs:
    controller = klass(app, route)
    controller.add_url_rules()


def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
