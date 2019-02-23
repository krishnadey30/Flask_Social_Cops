import falcon

api = application = falcon.API()

upload_data = upload_data()
stop = stop()
# Add a route to serve the resource
api.add_route('/upload', upload_data)
api.add_route('/stop',stop)