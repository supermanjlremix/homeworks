import threading
import os

def replace_words(
        filename: str, directory: str,
        word_to_replace: str, replacement_word: str=None) -> None:   
    new_filename = (os.path.splitext(filename)[0] 
                    + "_modifiedd" 
                    + os.path.splitext(filename)[1])
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r') as file:
        content = file.read()    
    modified_content = content.replace(
        word_to_replace, replacement_word
        )
    new_file_path = os.path.join(directory, new_filename)
    with open(new_file_path, 'w') as new_file:
        new_file.write(modified_content)


def process_files(files: list) -> None:
    threads = []
    for filename in files:
        thread = threading.Thread(
            target=replace_words, args=(
                filename, directory, word_to_replace, replacement_word
                )
            )
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


directory = 'folder'

try:
    word_to_replace, replacement_word = input(
    "Введите слово которое хотите заменить в формате Заменяемое Заменяющее: "
    ).split(" ")
except ValueError:
    print("Введите в формате <Заменяемое> на <Заменяющее> через пробел!")
    exit()
    
files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]







