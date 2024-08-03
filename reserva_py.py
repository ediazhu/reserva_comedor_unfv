import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Bienvenido a la aplicación para reservar comedor."
        return "La hora actual es: #HORA"

cherrypy.quickstart(HelloWorld())