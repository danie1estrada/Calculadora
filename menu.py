# menu.py
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_menubar():
    menubar = Gtk.MenuBar.new()

    item_calc = Gtk.MenuItem.new_with_label('Calculadora')
    menu_calc = Gtk.Menu.new()

    item_modo = Gtk.MenuItem.new_with_label('Modo')
    menu_modo = Gtk.Menu.new()

    item_ayuda = Gtk.MenuItem.new_with_label('Ayuda')
    menu_ayuda = Gtk.Menu.new()

    item_copiar = Gtk.MenuItem.new_with_label('Copiar')
    item_pegar = Gtk.MenuItem.new_with_label('Pegar')
    item_deshacer = Gtk.MenuItem.new_with_label('Deshacer')
    item_rehacer = Gtk.MenuItem.new_with_label('Rehacer')
    item_preferencias = Gtk.MenuItem.new_with_label('Preferencias')
    item_salir = Gtk.MenuItem.new_with_label('Salir')

    item_basico = Gtk.MenuItem.new_with_label('Básico')
    item_avanzado = Gtk.MenuItem.new_with_label('Avanzado')
    item_financiero = Gtk.MenuItem.new_with_label('Financiero')
    item_programador = Gtk.MenuItem.new_with_label('Programador')

    item_indice = Gtk.MenuItem.new_with_label('Índice')
    item_obtener_ayuda = Gtk.MenuItem.new_with_label('Obtener ayuda en línea...')
    item_traducir = Gtk.MenuItem.new_with_label('Traducir esta aplicación...')
    item_acerca_de = Gtk.MenuItem.new_with_label('Acerca de')

    menu_calc.append(item_copiar)
    menu_calc.append(item_pegar)
    menu_calc.append(item_deshacer)
    menu_calc.append(item_rehacer)
    menu_calc.append(Gtk.SeparatorMenuItem().new())
    menu_calc.append(item_preferencias)
    menu_calc.append(Gtk.SeparatorMenuItem().new())
    menu_calc.append(item_salir)

    menu_modo.append(item_basico)
    menu_modo.append(item_avanzado)
    menu_modo.append(item_financiero)
    menu_modo.append(item_programador)

    menu_ayuda.append(item_indice)
    menu_ayuda.append(Gtk.SeparatorMenuItem().new())
    menu_ayuda.append(item_obtener_ayuda)
    menu_ayuda.append(item_traducir)
    menu_ayuda.append(Gtk.SeparatorMenuItem().new())
    menu_ayuda.append(item_acerca_de)

    item_calc.set_submenu(menu_calc)
    item_modo.set_submenu(menu_modo)
    item_ayuda.set_submenu(menu_ayuda)

    menubar.append(item_calc)
    menubar.append(item_modo)
    menubar.append(item_ayuda)

    return menubar