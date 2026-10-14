# Build valid HTTP status lines, headers, and bodies

def create_response(http_method, path):
    if http_method == "GET":
        if path == "/":
            with open("public/index.html", "r") as file:
                content = file.read()

            response = "HTTP/1.1 200 OK\r\n\r\n" + content

        else:
            response = (
                "HTTP/1.1 404 Not Found\r\n\r\n"
                "<h1>404 Not Found</h1>"
            )
    else:
        response = (
            "HTTP/1.1 405 Method Not Allowed\r\n\r\n"
            "<h1>405 Method Not Allowed</h1>"
        )
    return response