import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def calcola_anagrammi(self, e):
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        parolaInserita = self._view.txt_word.value
        if parolaInserita is None or parolaInserita == "":
            self._view.create_alert("Attenzione: inserisci una parola!")
            self._view.update_page()
            return
        setSoluzioni = self._model.calcola_anagrammi(parolaInserita)
        listaParoleDB = self._model.listParole
        self._view.lst_correct.controls.append(ft.Text("Le parole valide che appartengono al dizionario sono:"))
        self._view.lst_wrong.controls.append(ft.Text("Le parole non valide sono:"))
        for parola in setSoluzioni:
            if parola in listaParoleDB:
                self._view.lst_correct.controls.append(ft.Text(parola))
            else:
                self._view.lst_wrong.controls.append(ft.Text(parola))
        self._view.update_page()
        return

    def reset(self, e):
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        self._view.lst_correct.controls.append(ft.Text("----"))
        self._view.lst_wrong.controls.append(ft.Text("----"))
        self._view.txt_word.value = ""
        self._view.update_page()
        return

