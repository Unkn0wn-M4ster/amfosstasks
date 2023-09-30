import sys
import requests
import random
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout , QDialog , QScrollArea
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

class PokemonDisplayWindow(QDialog):
    def __init__(self, captured_pokemons):
        super().__init__()
        self.setWindowTitle("Captured Pokémon")
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for pokemon_name, image_path in captured_pokemons:
            name_label = QLabel(f"Captured: {pokemon_name}")
            scroll_layout.addWidget(name_label)

            pixmap = QPixmap(image_path)
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            scroll_layout.addWidget(image_label)

        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        self.setLayout(layout)
        
class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.captured_pokemons = []  # List to store the names of captured pokemons
        self.current_index = 0
        
        main_layout = QVBoxLayout()

        background_label = QLabel(self)
        pixmap = QPixmap('landing.jpg')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True) 
        main_layout.addWidget(background_label, stretch=5)

        search_layout = QVBoxLayout()

        label1 = QLabel("Enter the name")
        search_layout.addWidget(label1)

        self.textbox = QLineEdit()
        search_layout.addWidget(self.textbox)

        # Create a QHBoxLayout for the buttons
        buttons_layout = QHBoxLayout()

        enter_button = QPushButton("Search")
        enter_button.clicked.connect(self.Search_Pokemon)
        enter_button.setFixedWidth(100)
        enter_button.setFixedHeight(30)
        buttons_layout.addWidget(enter_button)

        enter_button = QPushButton("Capture")
        enter_button.clicked.connect(self.Capture_Pokemon)
        enter_button.setFixedWidth(100)
        enter_button.setFixedHeight(30)
        buttons_layout.addWidget(enter_button)
        
        enter_button = QPushButton("Display")
        enter_button.clicked.connect(self.display_pokemon)
        enter_button.setFixedWidth(100)
        enter_button.setFixedHeight(30)
        buttons_layout.addWidget(enter_button)

        search_layout.addLayout(buttons_layout)  # Add the buttons layout

        search_layout.setContentsMargins(50, 0, 50, 0)
        main_layout.addLayout(search_layout)

        info_layout = QVBoxLayout()

        self.name_label = QLabel()
        self.name_label.setFont(QFont("Arial", 16))  
        info_layout.addWidget(self.name_label)

        self.abilities_label = QLabel()
        self.abilities_label.setFont(QFont("Arial", 14)) 
        info_layout.addWidget(self.abilities_label)

        self.types_label = QLabel()
        self.types_label.setFont(QFont("Arial", 14))  
        info_layout.addWidget(self.types_label)

        self.stats_label = QLabel()
        self.stats_label.setFont(QFont("Arial", 14))  
        info_layout.addWidget(self.stats_label)

        pokemon_info_layout = QHBoxLayout()

        self.pokemon_image_label = QLabel()
        pokemon_info_layout.addWidget(self.pokemon_image_label)

        pokemon_info_layout.addLayout(info_layout)

        main_layout.addLayout(pokemon_info_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("Pokemon Search")
        



    def Search_Pokemon(self):
        search_text = self.textbox.text()
        url = f'https://pokeapi.co/api/v2/pokemon/{search_text.lower()}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            name = data['name']
            abilities = [ability['ability']['name'] for ability in data['abilities']]
            types = [type_info['type']['name'] for type_info in data['types']]
            stats = [(stat['stat']['name'], stat['base_stat']) for stat in data['stats']]


            self.name_label.setText(f"Name: {name}")
            
            self.abilities_label.setText(f"Abilities: {', '.join(abilities)}")
            
            self.types_label.setText(f"Types: {', '.join(types)}")
            
            stats_text = "\n".join([f"{stat_name}: {base_stat}" for stat_name, base_stat in stats])
            
            self.stats_label.setText(f"Stats:\n{stats_text}")

            sprite_url = data['sprites']['other']['official-artwork']['front_default']
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(sprite_url).content)
            scaled_pixmap = pixmap.scaled(300, 300)
            self.pokemon_image_label.setPixmap(scaled_pixmap)


        elif response.status_code == 404:
            self.name_label.setText("Error: Pokemon not found")
            self.abilities_label.clear()
            self.types_label.clear()
            self.stats_label.clear()
            self.pokemon_image_label.clear()
            
            
        else:
            self.name_label.setText(f"Error: {response.status_code}, Unable to fetch data")




    def Capture_Pokemon(self):
        search_text = self.textbox.text()
        url = f'https://pokeapi.co/api/v2/pokemon/{search_text.lower()}'
        response = requests.get(url)

        # Determine if the capture is successful with a 1/3 probability
        capture_successful = random.random() <= 1/3

        if capture_successful and response.status_code == 200:
            data = response.json()
            name = data['name']

            folder_name = "Pokemans"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            sprite_url = data['sprites']['other']['official-artwork']['front_default']
            response = requests.get(sprite_url)
            
            if response.status_code == 200:
                with open(f"{folder_name}/{name}.png", "wb") as file:
                    file.write(response.content)
                self.name_label.setText(f"Captured: {name}")
            
            else:
                self.name_label.setText("Error: Unable to capture Pokemon image")
        
        elif response.status_code == 404:
            self.name_label.setText("Error: Pokemon not found")
            self.abilities_label.clear()
            self.types_label.clear()
            self.stats_label.clear()
            self.pokemon_image_label.clear()
        
        else:
            self.name_label.setText(f"Catch Failed Try again ")


    def display_pokemon(self):
        folder_name = "Pokemans"
        captured_files = os.listdir(folder_name)
        self.captured_pokemons = [(file.split('.')[0], os.path.join(folder_name, file)) for file in captured_files if file.endswith('.png')]

        if not self.captured_pokemons:
            self.show_message_box("No captured Pokémon found.")
        else:
            display_window = PokemonDisplayWindow(self.captured_pokemons)
            display_window.exec_()

        
    def capture_pokemon(self, pokemon_name, image_path):
        self.captured_pokemons.append((pokemon_name, image_path))

    def view_captured_pokemon(self):
        display_window = PokemonDisplayWindow(self.captured_pokemons)
        display_window.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())

