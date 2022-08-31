from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)  # runs the web server, debug=True reruns the server after changes
        # host="localhost", port=8000... from
        #   https://stackoverflow.com/questions/41940663/how-can-i-change-the-host-and-port-that-the-flask-command-uses






