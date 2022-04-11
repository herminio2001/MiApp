import web

urls = (
    '/login', 'mvc.controllers.public.login.Login',
    '/index', 'mvc.controllers.public.index.Index',
    '/list_user', 'mvc.controllers.public.list_user.List_user',
    '/registrar', 'mvc.controllers.public.registrar.Registrar',
    '/principal', 'mvc.controllers.public.principal.Principal',
    '/dash', 'mvc.controllers.public.dash.Dash',
    '/update', 'mvc.controllers.public.update.Update',
    '/login_ope', 'mvc.controllers.public.login_ope.Login_ope',
    '/principal_ope', 'mvc.controllers.public.principal_ope.Principal_ope',
    '/recuperar_con', 'mvc.controllers.public.recuperar_con.Recuperar_con',
)       
 
app = web.application(urls, globals())  
        
if __name__ == "__main__":
    web.config.debug = True
    app.run()