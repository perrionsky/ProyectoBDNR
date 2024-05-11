import model
import pydgraph
import os


# Configurar la URI de Dgraph desde una variable de entorno o valor por defecto
DGRAPH_URI = os.getenv('DGRAPH_URI', 'localhost:9080')

def print_menu():
    menu_options = {
        1: "Search Trend by Name",
        2: "Search Trend by Country",
        3: "Add New Trend",
        4: "Delete Trend by Name",
        5: "Save Changes to JSON",
        6: "Exit"
    }
    for key, value in menu_options.items():
        print(f"{key} - {value}")

def main():
    client_stub = model.create_client_stub(DGRAPH_URI)
    client = model.create_client(client_stub)
    
    try:
        model.set_schema(client)
        
        # Menú para interactuar con el usuario
        while True:
            print("1. Añadir nueva tendencia")
            print("2. Buscar tendencias por país")
            print("3. Salir")
            choice = input("Ingrese su elección: ")
            
            if choice == '1':
                trend_data = {
                    'name': input("Ingrese el nombre de la tendencia: "),
                    'url': input("Ingrese la URL: "),
                    'query': input("Ingrese la consulta: "),
                    'tweet_volume': int(input("Ingrese el volumen de tweets: ")),
                    'searched_at_datetime': input("Ingrese la fecha y hora de búsqueda: "),
                    'searched_in_country': input("Ingrese el país de búsqueda: ")
                }
                model.add_trend(client, trend_data)
            elif choice == '2':
                country = input("Ingrese el país para buscar tendencias: ")
                results = model.search_trends_by_country(client, country)
                print(results)
            elif choice == '3':
                break
            else:
                print("Opción no válida.")
        
    finally:
        client_stub.close()

if __name__ == '__main__':
    main()
