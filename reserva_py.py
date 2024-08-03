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
                <h1>RESERVAR COMEDOR UNFV-RADIOLOGIA</h1>
                <form action="generar_link" method="post">
                    <label>Ingrese su codigo de estudiante.</label>
                    <input type="text" name="numero" />
                    <button type="submit" name="turno" value="1">Generar para 1er Turno</button>
                    <button type="submit" name="turno" value="2">Generar para 2do Turno</button>
                </form>
                <p>¿Cómo funciona esto? <a href="como_funciona">Haz clic aquí</a></p>
                <p>La hora del sistema es: {}</p>
                <p>Se recomienda reservar a partir de las 11:01 am y no antes</p>
            </body>
        </html>
        """.format(hora_actual)

    @cherrypy.expose
    def generar_link(self, numero, turno):
        if turno == "1":
            link_personalizado = f"https://example.com/link/turno1/{numero}/hahaha"
            return f"""
            <html>
                <body>
                    <h1>Ud Ha seleccionado el 1er Turno: 12:00am a 1:30pm</h1>
                    <p>Haga clic aqui para reservar: <a href="{link_personalizado}" target="_blank">{link_personalizado}</a></p>
                    <p><a href="index">Regresar a la página principal</a></p>
                </body>
            </html>
            """
        elif turno == "2":
            link_personalizado = f"https://example.com/link/turno2/{numero}"
            return f"""
            <html>
                <body>
                    <h1>Ud Ha seleccionado el 1er Turno: 1:30pm a 2:15pm/h1>
                    <p>Haga clic aqui para reservar: <a href="{link_personalizado}" target="_blank">{link_personalizado}</a></p>
                    <p><a href="index">Regresar a la página principal</a></p>
                </body>
            </html>
            """

    @cherrypy.expose
    def como_funciona(self):
        return """
        <html>
            <body>
                <h1>¿Cómo funciona esto? ¿Que gano con esto?</h1>
                <p>Pues solo permite generar un link directo a reserva de comedor.</p>
                <p>El objetivo de esta pequeña app es saltar el procedimiento comun para reserva, 
                    dado que la web oficial se colapsa al reservar. Para evitar la espera y la posterior perdida
                    de cupo, se hizo esta app.
                </p>
                <p>
                    La app corre en Python bajo el framework CherryPy. Luego se añadirá CSS.
                </p>
                <p> <i>Hecho por algun estudiante de Radiologia-UNFV </i></p>
                <p><a href="index">Regresar a la página principal</a></p>
            </body>
        </html>
        """

if __name__ == '__main__':
    cherrypy.quickstart(Formulario())