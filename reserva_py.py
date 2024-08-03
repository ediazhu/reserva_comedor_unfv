import cherrypy
import datetime
import pytz

class Formulario:
    @cherrypy.expose
    def index(self):
        zona_horaria = pytz.timezone('America/Lima')
        fecha_hora_actual = datetime.datetime.now(zona_horaria)
        hora_actual = fecha_hora_actual.strftime('%H:%M:%S')
        return """
        <html>
            <body>
                <h1>Generador de links personalizados</h1>
                <form action="generar_link" method="post">
                    <label>Ingrese un número:</label>
                    <input type="text" name="numero" />
                    <button type="submit" name="turno" value="1">Generar Link para el 1er turno</button>
                    <button type="submit" name="turno" value="2">Generar Link para el 2do turno</button>
                </form>
                <p>¿Cómo funciona esto? <a href="como_funciona">Haz clic aquí</a></p>
                <p>La hora del sistema es: {}</p>
                <p>Se recomienda reservar a partir de las 11:01 y no antes</p>
            </body>
        </html>
        """.format(hora_actual)

    @cherrypy.expose
    def generar_link(self, numero, turno):
        if turno == "1":
            link_personalizado = f"https://example.com/link/turno1/{numero}"
            return f"""
            <html>
                <body>
                    <h1>Link personalizado generado para el 1er turno</h1>
                    <p>Su link personalizado es: <a href="{link_personalizado}" target="_blank">{link_personalizado}</a></p>
                </body>
            </html>
            """
        elif turno == "2":
            link_personalizado = f"https://example.com/link/turno2/{numero}"
            return f"""
            <html>
                <body>
                    <h1>Link personalizado generado para el 2do turno</h1>
                    <p>Su link personalizado es: <a href="{link_personalizado}" target="_blank">{link_personalizado}</a></p>
                </body>
            </html>
            """

    @cherrypy.expose
    def como_funciona(self):
        return """
        <html>
            <body>
                <h1>¿Cómo funciona esto?</h1>
                <p>Esta página permite generar links personalizados con un código adicional.</p>
                <p>Simplemente ingrese un número en el formulario y haga clic en "Generar Link para el 1er turno" o "Generar Link para el 2do turno".</p>
            </body>
        </html>
        """

if __name__ == '__main__':
    cherrypy.quickstart(Formulario())