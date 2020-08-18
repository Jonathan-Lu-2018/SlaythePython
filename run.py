from app import create_app
apps = create_app()

if __name__ == '__main__':
    apps.run(debug=True)
    