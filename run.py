from app import create_app
# Crear la aplicación Flask
app = create_app()
# Ejecutar la aplicación si este archivo es ejecutado directamente
if __name__ == "__main__":
    app.run(debug=True)