from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

# permet de charger un fichier kv
Builder.load_file("widget_exemples.kv")


class WidgetsExemple(GridLayout):
    compteur = 1
    # utilisation de StringProperty , BooleanProperty, ... pour pouvoir les utiliser
    # dans le fichier kv avec root.mon_texte, root.compteur_actif, ...
    mon_texte = StringProperty(str(compteur))
    compteur_actif = BooleanProperty(False)
    text_input_str = StringProperty("Toto")

    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self, widget):
        print("Toggle state: " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, widget):
        print("Switch active: " + str(widget.active))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
