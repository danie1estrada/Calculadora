import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Calculadora(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")

        self.texto = ""
        self.grid = Gtk.Grid()
        self.pantalla = Gtk.Entry()

        self.btn_0 = Gtk.Button(label="0")
        self.btn_1 = Gtk.Button(label="1")
        self.btn_2 = Gtk.Button(label="2")
        self.btn_3 = Gtk.Button(label="3")
        self.btn_4 = Gtk.Button(label="4")
        self.btn_5 = Gtk.Button(label="5")
        self.btn_6 = Gtk.Button(label="6")
        self.btn_7 = Gtk.Button(label="7")
        self.btn_8 = Gtk.Button(label="8")
        self.btn_9 = Gtk.Button(label="9")

        self.btn_suma           = Gtk.Button(label="+")
        self.btn_resta          = Gtk.Button(label="-")
        self.btn_division       = Gtk.Button(label="÷")
        self.btn_multiplicacion = Gtk.Button(label="×")
        self.btn_modulo         = Gtk.Button(label="%")
        self.btn_raiz           = Gtk.Button(label="√")
        self.btn_aparentesis    = Gtk.Button(label="(")
        self.btn_cparentesis    = Gtk.Button(label=")")
        self.btn_punto          = Gtk.Button(label=".")
        self.btn_igual          = Gtk.Button(label="=")
        self.btn_limpiar        = Gtk.Button(label="C")
        self.btn_borrar         = Gtk.Button(label="<=")
        self.btn_exponente      = Gtk.Button(label="x²")

        self.propiedades()
        self.escuchas()
        self.armar()

    def propiedades(self):
        self.set_resizable(False)

        self.pantalla.set_max_length(35)
        self.pantalla.set_editable(False)
        self.pantalla.set_can_focus(False)
        self.pantalla.set_margin_bottom(5)

        self.grid.set_row_spacing(4)
        self.grid.set_column_spacing(4)

        self.grid.set_margin_top(10)
        self.grid.set_margin_left(10)
        self.grid.set_margin_right(10)
        self.grid.set_margin_bottom(10)

        self.btn_0.set_can_focus(False)
        self.btn_1.set_can_focus(False)
        self.btn_2.set_can_focus(False)
        self.btn_3.set_can_focus(False)
        self.btn_4.set_can_focus(False)
        self.btn_5.set_can_focus(False)
        self.btn_6.set_can_focus(False)
        self.btn_7.set_can_focus(False)
        self.btn_8.set_can_focus(False)
        self.btn_9.set_can_focus(False)
        self.btn_suma.set_can_focus(False)
        self.btn_resta.set_can_focus(False)
        self.btn_division.set_can_focus(False)
        self.btn_multiplicacion.set_can_focus(False)
        self.btn_modulo.set_can_focus(False)
        self.btn_raiz.set_can_focus(False)
        self.btn_aparentesis.set_can_focus(False)
        self.btn_cparentesis.set_can_focus(False)
        self.btn_punto.set_can_focus(False)
        self.btn_igual.set_can_focus(False)
        self.btn_limpiar.set_can_focus(False)
        self.btn_borrar.set_can_focus(False)
        self.btn_exponente.set_can_focus(False)

    def armar(self):
        self.add(self.grid)

        self.grid.attach(self.pantalla, 0, 0, 6, 1)

        self.grid.attach(self.btn_7,        0, 1, 1, 1)
        self.grid.attach(self.btn_8,        1, 1, 1, 1)
        self.grid.attach(self.btn_9,        2, 1, 1, 1)
        self.grid.attach(self.btn_division, 3, 1, 1, 1)
        self.grid.attach(self.btn_borrar,   4, 1, 1, 1)
        self.grid.attach(self.btn_limpiar,  5, 1, 1, 1)

        self.grid.attach(self.btn_4,              0, 2, 1, 1)
        self.grid.attach(self.btn_5,              1, 2, 1, 1)
        self.grid.attach(self.btn_6,              2, 2, 1, 1)
        self.grid.attach(self.btn_multiplicacion, 3, 2, 1, 1)
        self.grid.attach(self.btn_aparentesis,    4, 2, 1, 1)
        self.grid.attach(self.btn_cparentesis,    5, 2, 1, 1)

        self.grid.attach(self.btn_1,         0, 3, 1, 1)
        self.grid.attach(self.btn_2,         1, 3, 1, 1)
        self.grid.attach(self.btn_3,         2, 3, 1, 1)
        self.grid.attach(self.btn_resta,     3, 3, 1, 1)
        self.grid.attach(self.btn_exponente, 4, 3, 1, 1)
        self.grid.attach(self.btn_raiz,      5, 3, 1, 1)

        self.grid.attach(self.btn_0,      0, 4, 1, 1)
        self.grid.attach(self.btn_punto,  1, 4, 1, 1)
        self.grid.attach(self.btn_modulo, 2, 4, 1, 1)
        self.grid.attach(self.btn_suma,   3, 4, 1, 1)
        self.grid.attach(self.btn_igual,  4, 4, 2, 1)

    def escuchas(self):
        self.btn_0.connect("clicked", self.btn_clicked)
        self.btn_1.connect("clicked", self.btn_clicked)
        self.btn_2.connect("clicked", self.btn_clicked)
        self.btn_3.connect("clicked", self.btn_clicked)
        self.btn_4.connect("clicked", self.btn_clicked)
        self.btn_5.connect("clicked", self.btn_clicked)
        self.btn_6.connect("clicked", self.btn_clicked)
        self.btn_7.connect("clicked", self.btn_clicked)
        self.btn_8.connect("clicked", self.btn_clicked)
        self.btn_9.connect("clicked", self.btn_clicked)

        self.btn_suma.connect("clicked", self.btn_clicked)
        self.btn_resta.connect("clicked", self.btn_clicked)
        self.btn_division.connect("clicked", self.btn_clicked)
        self.btn_multiplicacion.connect("clicked", self.btn_clicked)

        self.btn_punto.connect("clicked", self.btn_clicked)
        self.btn_modulo.connect("clicked", self.btn_clicked)
        self.btn_exponente.connect("clicked", self.btn_clicked)

        self.btn_aparentesis.connect("clicked", self.btn_clicked)
        self.btn_cparentesis.connect("clicked", self.btn_clicked)

        self.btn_borrar.connect("clicked", self.borrar)
        self.btn_igual.connect("clicked", self.calcular)
        self.btn_limpiar.connect("clicked", self.limpiar_pantalla)

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
            # self.texto = ""
            self.mostrar_error("Expresión no válida")
        except ZeroDivisionError:
            # self.texto = ""
            self.mostrar_error("División entre cero")
        finally:
            self.pantalla.set_text(self.texto)

    def mostrar_error(self, mensaje):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
        Gtk.ButtonsType.OK, "Error: {}.".format(mensaje))
        dialog.run()
        dialog.destroy()

    def key_controller(self, widget, event):
        n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "%",
        "(", ")", "."]

        if event.string in n:
            if len(self.texto) < 35:
                self.texto += event.string
            self.pantalla.set_text(self.texto)
        elif event.hardware_keycode == 36 or event.hardware_keycode == 104:
            self.calcular(widget)
        elif event.hardware_keycode == 22:
            self.borrar(widget)
        elif event.string == "*":
            if len(self.texto) < 35:
                self.texto += "×"
            self.pantalla.set_text(self.texto)
        elif event.string == "/":
            if len(self.texto) < 35:
                self.texto += "÷"
            self.pantalla.set_text(self.texto)

if __name__ == "__main__":
    calc = Calculadora()
    calc.show_all()
    Gtk.main()