import json


def add_key_value_pair(container_name, label, id, json_file_var):
    with open(json_file_var, "r") as json_file:
        data = json.load(json_file)

    id = id.strip()

    data[container_name][label] = id

    with open(json_file_var, 'w') as json_file:
        json_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

    print("Successfuly wrote JSON data")


def remove_key_value_pair(container_name, label, json_file_var):
    with open(json_file_var, "r") as json_file:
        data = json.load(json_file)

    del data[container_name][label]

    with open(json_file_var, 'w') as json_file:
        json_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

    print("Successfuly wrote JSON data")
