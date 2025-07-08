from app import app , db




@app.cli.command
def init():
    db.create_all()
    print('db ok !!')


if __name__ == '__main':
    app.run()