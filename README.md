# codio-zootopia-api-gh


This project generates a simple HTML page displaying information about animals fetched from the Animal API(https://api-ninjas.com/api/animals).

## Overview
The HTMLCreator class takes an animal name as input, calls an external API to retrieve information about that animal (or related animals), and then generates an HTML file (animals.html) by populating a template (animals_template.html) with the fetched data.


## How to use

> [!CAUTION] To install this project, simply clone the repository and install the dependencies in requirements.txt using `pip`

- run animals_web_generator.py

- Type an animal name (e.g., lion, tiger, bear) and press Enter.

- After execution, an animals.html file will be created in the same directory. Open this file in your web browser to see the generated animal information.

> Error Handling: Displays a message if the searched animal is not found.

(c) 2025 Justus Decker