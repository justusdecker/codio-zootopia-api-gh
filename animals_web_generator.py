
from modules.animals_api import animal_api_call, Animal
class HTMLCreator:
    def __init__(self,search: str):
        self.search = search
    def serialize_animal(self, animal: Animal):
        typ_ext = f"\n<strong>Type: </strong>\n{animal.type}<br>" if animal.type else ''
        return f'<li class="cards__item"><div class="card__title">{animal.name}</div>\n<p class="card__text">\n<strong>Diet: </strong>{animal.diet}<br>\n<strong>Location: </strong>{animal.first_location}<br>{typ_ext}\n</p>\n</li>\n'

    def serialize_html(self, path_input:str, path_output: str) -> None:
        with open(path_input,'r') as file_in:
            html = file_in.read()
        html = html.replace('__REPLACE_ANIMALS_INFO__',self.generate_unsorted_list())
        with open(path_output,'w') as file_out:
            file_out.write(html)
        print("Website was successfully generated to the file animals.html.")
            
    def generate_unsorted_list(self):
        html_string = ''
        api_ret = animal_api_call(self.search)
        if not api_ret:
             return f'<h2>{self.search} doesn\'t exist.</h2>'
        for animal in api_ret:
            html_string += self.serialize_animal(Animal(animal))

        return html_string
def main():
    user_input = ''
    while not user_input:
        user_input = input('Enter a name of an animal: ')
    APP = HTMLCreator(user_input)
    APP.serialize_html('animals_template.html','animals.html')
if __name__ == '__main__':
    main()