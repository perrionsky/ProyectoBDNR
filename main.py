import model
import pydgraph

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
    df = model.load_data('/path/to/csvjson.json')
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            trend_name = input("Enter trend name to search: ")
            results = model.search_trend(df, trend_name)
            print(results)
        elif choice == 2:
            country_name = input("Enter country name to search: ")
            results = model.search_trend_by_country(df, country_name)
            print(results)
        elif choice == 3:
            trend_data = {
                "trend_name": input("Enter trend name: "),
                "trend_url": input("Enter trend URL: "),
                "trend_query": input("Enter trend query: "),
                "tweet_volume": input("Enter tweet volume: "),
                "searched_at_datetime": input("Enter datetime: "),
                "searched_in_country": input("Enter country: ")
            }
            df = model.add_trend(df, trend_data)
            print("Trend added successfully.")
        elif choice == 4:
            trend_name = input("Enter trend name to delete: ")
            df = model.delete_trend(df, trend_name)
            print("Trend deleted successfully.")
        elif choice == 5:
            model.save_data(df, '/path/to/modified_csvjson.json')
            print("Data saved successfully.")
        elif choice == 6:
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
