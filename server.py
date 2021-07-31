from flask import Flask, request, redirect
from mongo import MongoConnection
from helper.helper import Helper, getLongUrl

app = Flask(__name__)

mongo = MongoConnection()


@app.route("/short-url")
def shorten_url():
    """
    1. take in long url and search db
    2. if url present, return existing data
    3. if url not present, create new record
    """

    try:
        url = request.args.get("url")

        query = {"longUrl": url}
        data = mongo.find(query)
        if data is not None:
            del data["_id"]
            result = {"success": True, "data": data}
            return result, 200
        else:
            # create new record
            host_name = request.url_root
            helper = Helper(url, host_name)
            urlObj = helper.getShortUrl()
            return {"success": True, "data": urlObj}, 200
    except Exception as e:
        print(e)
        return {"success": False, "err": str(e)}


@app.route("/<short_code>")
def redirect_url(short_code):
    print(short_code)
    long_url = getLongUrl(short_code)
    if long_url is not None:
        return redirect(long_url, code=302)
    else:
        return "page not found", 404

