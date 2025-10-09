from project import create_app
#   this is just for test
if __name__ == '__main__':
    app = create_app()
    app.run(debug = True, port=8888)
    