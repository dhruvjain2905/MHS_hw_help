from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    #app.run(host="192.168.1.162", port=5000)