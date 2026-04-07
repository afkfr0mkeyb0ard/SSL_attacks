from flask import Flask, request, Response
import gzip
import io

app = Flask(__name__)

SECRET = "SECRET_TOKEN_TRYFINDME"

@app.route("/")
def index():
    q = request.args.get("q", "")

    # vulnerable code here
    body = f"token={SECRET}&token={q}"

    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb") as f:
        f.write(body.encode())

    compressed = buf.getvalue()

    return Response(compressed, headers={
        "Content-Encoding": "gzip",
        "Content-Length": str(len(compressed))
    })

app.run(port=5000)
