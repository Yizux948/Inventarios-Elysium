# CERRAR SESIÓN
def close_session(root, app):
    app.destroy()
    root.deiconify()