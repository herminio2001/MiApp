import web

urls = (
    '/login', 'mvc.controllers.public.login.Login',
    '/index', 'mvc.controllers.public.index.Index', 
    #'/list_user', 'mvc.controllers.public.list.List_user'
)       
 
app = web.application(urls, globals())  
        
if __name__ == "__main__":
    web.config.debug = True
    app.run()