import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def print_header():
    print('-----------------------------------')
    print('         TEXT SEARCH APP')
    print('-----------------------------------')  


def main():
    print_header()
    folder = ask_user_for_folder()
    if not folder:                                      
        print('You have to specify a folder to search in!')
        return

    text = ask_user_for_text()
    if not text:
        print('You have to specify some text to search!')
        return 

    matches = search_in_folder(folder, text) # get a list of all found matches 
    matches_count = 0
    for m in matches:                     
        matches_count += 1
        print('--------- MATCH ---------------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()
    
    print("Found {:,} matches".format(matches_count))
    

def ask_user_for_folder():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip(): 
        return None
    
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def ask_user_for_text():    
    text = input('What are you searching for? [single phrases only] ')
    return text.lower()


def search_in_folder(folder, text):
    """
        Takes the folder specified by user and then gets every item of this folder.
        If folder is found: perfoms NOTHING (FOR NOW)
        If file is found: gets the full path to this file by joining its name and a full path to folder
    """
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item): 
            yield from search_in_folder(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, text):
    try:
        with open(filename, 'r', encoding='utf-8') as src:

            line_num = 0
            for line in src:
                line_num += 1
                if line.lower().find(text) >= 0:
                    full_result = SearchResult(file=filename, line=line_num , text=line)
                    yield full_result

    except UnicodeDecodeError:
        print("NOTICE: Binary file {} skipped.".format(filename))


if __name__ == "__main__":
    main()

