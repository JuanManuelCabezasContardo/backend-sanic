from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import json
from api_function import ping,report
app = Sanic("MyHelloWorldApp")

class Email(HTTPMethodView):
    async def get(self,request,hostname):
        if hostname!= None:
            return json(ping(hostname))
    async def post(self, request):
        try:
            data =request.json
            if (data):
                return json(report(data))
        except Exception as error:
            return json({"error":"cago"})
        
        
Email_view =Email.as_view()
app.add_route(Email_view,"/report/<hostname>",methods=["GET"])
app.add_route(Email_view, "/email/")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,workers=10)