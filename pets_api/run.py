from pets_api.papi.resources import api, app

# init restful api
api.init_app(app)

if __name__ == "__main__":
    app.run()

