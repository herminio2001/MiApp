import web
import app

render = web.template.render("mvc/view/public", base="layout")

class Index:

    def GET(self):
        return render.index()
