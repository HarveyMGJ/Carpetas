# Estructura de carpetas
carpeta_raiz = {
    "nombre": "Raíz",
    "subcarpetas": [
        {
            "nombre": "Documentos",
            "subcarpetas": [
                {"nombre": "Proyectos", "subcarpetas": []},
                {"nombre": "Informes", "subcarpetas": []}
            ]
        },
        {
            "nombre": "Fotos",
            "subcarpetas": [
                {
                    "nombre": "Vacaciones",
                    "subcarpetas": [
                        {"nombre": "Playa", "subcarpetas": []},
                        {"nombre": "Montaña", "subcarpetas": []}
                    ]
                },
                {"nombre": "Eventos", "subcarpetas": []}
            ]
        },
        {
            "nombre": "Música",
            "subcarpetas": [
                {"nombre": "Rock", "subcarpetas": []},
                {"nombre": "Jazz", "subcarpetas": []}
            ]
        }
    ]
}

# Función para navegar por las carpetas
def navegar_carpeta(carpeta):
    while True:
        print(f"\n📂 Carpeta actual: {carpeta['nombre']}")
        subcarpetas = carpeta.get("subcarpetas", [])
        
        if not subcarpetas:
            print("📁 Esta carpeta no contiene subcarpetas.")
            break
        
        # Mostrar subcarpetas disponibles
        for i, sub in enumerate(subcarpetas):
            print(f"{i + 1}. {sub['nombre']}")
        print("0. Volver")

        # Leer opción del usuario
        try:
            opcion = int(input("Elige una carpeta para abrir: "))
        except ValueError:
            print("⚠️ Ingresa un número válido.")
            continue

        if opcion == 0:
            break
        elif 1 <= opcion <= len(subcarpetas):
            navegar_carpeta(subcarpetas[opcion - 1])
        else:
            print("⚠️ Opción fuera de rango.")

# Ejecutar desde la raíz
navegar_carpeta(carpeta_raiz)

