import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'


# Write to Json file
def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


# Load json file
def load_data(filepath):
    # Try and load file, return empty dictionary if not found.
    try:

        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

# Delete json file contents


def delete_data(filepath, data):

    with open(filepath, 'r') as fp:
        data = json.load(fp)
    del data['law'][1]

    with open(filepath, 'w') as fp:
        json.dump(data, fp)


# save_data("test.json ", {'key': 'value'})

if len(sys.argv) == 2:

    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key:')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data saved!')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print('key does not exist!')
    elif command == 'delete':
        key = input('Enter a key :')
        if key in data:
            print('Key is found')

        else:
            print('Key could not not be found')

    elif command == 'list':
        print(data)
    else:
        print('unknown command')
else:
    print('please pass exactly one argument')
