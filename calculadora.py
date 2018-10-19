# calculadora.py
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from menu import create_menubar

class Calculadora(Gtk.Window):

    # Constructor
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")

        self.texto = ""
        self.botones = []
        self.grid = Gtk.Grid()
        self.pantalla = Gtk.Entry()
        self.menubar = create_menubar()
        self.layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        simbolos = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "÷",
            "×", "%", "√", "(", ")", ".", "x²", "=", "←", "C"
        ]

        # Crea una arreglo de botones de acuerdo 
        for simbolo in simbolos:
            self.botones.append(Gtk.Button(label=simbolo))

        self.propiedades()
        self.escuchas()
        self.armar()

    def propiedades(self):
        # Propiedades de la ventana
        self.set_resizable(False)

        # Propiedades del Gtk.Entry 
        self.pantalla.set_max_length(35)
        self.pantalla.set_editable(False)
        self.pantalla.set_can_focus(False)
        self.pantalla.set_margin_bottom(5)

        # Propiedades del layout (Grid)
        self.grid.set_row_spacing(4)
        self.grid.set_column_spacing(4)
        self.grid.set_margin_top(10)
        self.grid.set_margin_left(10)
        self.grid.set_margin_right(10)
        self.grid.set_margin_bottom(10)

        # Propiedades de los botones
        for boton in self.botones:
            boton.set_can_focus(False)

        etiquetas = [
            "Suma", "Resta", "División", "Multiplicación", "Porcentaje", "Raíz",
            "Abrir paréntesis", "Cerrar paréntesis", "Punto decimal",
            "Exponente", "Resultado", "Borrar", "Borrar todo"
        ]

        for i in range(len(etiquetas)):
            self.botones[i + 10].set_tooltip_text(etiquetas[i])
        
    def armar(self):
        self.add(self.layout)
        self.layout.pack_end(self.grid, False, False, 0)
        self.layout.pack_start(self.menubar, False, False, 0)

        # attach: Elemento hijo, número de columna, número de fila, ancho, alto
        self.grid.attach(self.pantalla, 0, 0, 6, 1)

        self.grid.attach(self.botones[7],  0, 1, 1, 1)
        self.grid.attach(self.botones[8],  1, 1, 1, 1)
        self.grid.attach(self.botones[9],  2, 1, 1, 1)
        self.grid.attach(self.botones[12], 3, 1, 1, 1)
        self.grid.attach(self.botones[21], 4, 1, 1, 1)
        self.grid.attach(self.botones[22], 5, 1, 1, 1)

        self.grid.attach(self.botones[4],  0, 2, 1, 1)
        self.grid.attach(self.botones[5],  1, 2, 1, 1)
        self.grid.attach(self.botones[6],  2, 2, 1, 1)
        self.grid.attach(self.botones[13], 3, 2, 1, 1)
        self.grid.attach(self.botones[16], 4, 2, 1, 1)
        self.grid.attach(self.botones[17], 5, 2, 1, 1)

        self.grid.attach(self.botones[1],  0, 3, 1, 1)
        self.grid.attach(self.botones[2],  1, 3, 1, 1)
        self.grid.attach(self.botones[3],  2, 3, 1, 1)
        self.grid.attach(self.botones[11], 3, 3, 1, 1)
        self.grid.attach(self.botones[19], 4, 3, 1, 1)
        self.grid.attach(self.botones[15], 5, 3, 1, 1)

        self.grid.attach(self.botones[0],  0, 4, 1, 1)
        self.grid.attach(self.botones[18], 1, 4, 1, 1)
        self.grid.attach(self.botones[14], 2, 4, 1, 1)
        self.grid.attach(self.botones[10], 3, 4, 1, 1)
        self.grid.attach(self.botones[20], 4, 4, 2, 1)

    def escuchas(self):
        for i in range(20):
            self.botones[i].connect("clicked", self.btn_clicked)

        self.botones[20].connect("clicked", self.calcular)
        self.botones[21].connect("clicked", self.borrar)
        self.botones[22].connect("clicked", self.limpiar_pantalla)

        self.connect("key-press-event", self.key_controller)
        self.connect("destroy", Gtk.main_quit)

    def borrar(self, widget):
        self.texto = self.texto[:-1]
        self.pantalla.set_text(self.texto)

    def btn_clicked(self, widget):
        if len(self.texto) < 35:
            self.texto += widget.get_label()
            self.texto = self.texto.replace("x²", "^")

            self.pantalla.set_text(self.texto)

    def limpiar_pantalla(self, widget):
        self.texto = ""
        self.pantalla.set_text("")

    def calcular(self, widget):
        self.texto = self.texto.replace(")(", ")*(")
        self.texto = self.texto.replace("√", "**.5")
        self.texto = self.texto.replace("^", "**")
        self.texto = self.texto.replace("×", "*")
        self.texto = self.texto.replace("÷", "/")

        try:
            self.texto = str(eval(self.texto))
        except SyntaxError:
            self.mostrar_error("Expresión no válida")
        except ZeroDivisionError:
            self.mostrar_error("División entre cero")
        finally:
            self.pantalla.set_text(self.texto)

    def mostrar_error(self, mensaje):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
        Gtk.ButtonsType.OK, "Error: {}.".format(mensaje))
        dialog.run()
        dialog.destroy()

    def key_controller(self, widget, event):
        caracter = ""
        caracteres_permitidos = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "%",
            "(", ")", "."
        ]

        # Tecla 'Enter'
        if event.hardware_keycode == 36 or event.hardware_keycode == 104:
            self.calcular(widget)
        # Tecla 'Backspace
        elif event.hardware_keycode == 22:
            self.borrar(widget)
        else:
            if event.string in caracteres_permitidos:
                caracter = event.string
            elif event.string == "*":
                caracter = "×"
            elif event.string == "/":
                caracter= "÷"
            if len(self.texto) < 35 and caracter != "":
                self.texto += caracter
                self.pantalla.set_text(self.texto)

if __name__ == "__main__":
    calc = Calculadora()
    calc.show_all()
    Gtk.main()