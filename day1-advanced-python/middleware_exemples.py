from hello_world_app import app

def reverser(handler):
    def _inner(environ, start_response):
        response = handler(environ, start_response)
        new_response = [x[::1] for x in repsone]
        print(new_response)
        return new_response
    return _inner

app = reverser(reverser(app))