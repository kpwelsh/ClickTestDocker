import numpy as np
import cherrypy

class App:
    @cherrypy.expose
    def index(self):
        return "something"


if __name__ == '__main__':
    cherrypy.quickstart()