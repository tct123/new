import flet as ft

def main(page: ft.Page):
    # Definiere die verschiedenen Seiten
    def home_view():
        return ft.Column([ft.Text("Startseite")])

    def settings_view():
        return ft.Column([ft.Text("Einstellungen")])

    def profile_view():
        return ft.Column([ft.Text("Profil")])

    # Funktionen zum Wechseln der Ansichten
    def on_navigation_change(e):
        if e.control.selected_index == 0:
            page.content = home_view()
        elif e.control.selected_index == 1:
            page.content = settings_view()
        elif e.control.selected_index == 2:
            page.content = profile_view()
        page.update()

    # Definiere die NavigationBar
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        selected_index=0,
        on_change=on_navigation_change
    )

    # Füge die NavigationBar und die Startseite zur Seite hinzu
    page.navigation_bar = nav_bar
    page.content = home_view()

# Starte die App
ft.app(target=main)
