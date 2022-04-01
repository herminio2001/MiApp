import web

urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/sensores', 'mvc.controllers.public.Sensores.Sensores'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = True
    app.run()