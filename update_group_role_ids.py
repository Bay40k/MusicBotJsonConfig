import json
import os
import cfgparse  # used to edit ini in place without modifying things like comments

permissions_ini_location = 'permissions.ini'  # permissions.ini location for music bot
json_id_list_location = 'role_ids.json'  # role ids json, where Role Label/ID pair Json is located

config = cfgparse.ConfigParser()  # add parser
config_file = config.add_file(permissions_ini_location)  # add ini file


def main():
    with open(json_id_list_location) as json_binds_list:
        binds_json = json.load(json_binds_list)

    for key in binds_json:
        write_ids(print_ids(get_role_ids(key), key), key)
    return


def get_role_ids(role_name):
    with open(json_id_list_location) as json_binds_list:
        binds_json = json.load(json_binds_list)

    role_ids = []

    print("\nJson File: {}".format(os.path.realpath(json_id_list_location)))

    print("\n{} Role".format(role_name))
    print("Label : Role ID\n")

    role_id_table = binds_json[role_name]
    for key in role_id_table:
        value = role_id_table[key]
        print(key + " : " + value)
        role_ids.append(value)

    role_ids = " ".join(role_ids)

    return role_ids  # returns just our IDs, separated by space


def print_ids(role_ids, role_name):
    print("\nFile: '{}'".format(os.path.realpath(permissions_ini_location)))
    print("Existing role IDs")

    grant_to_role_setting = config.add_option("GrantToRoles", keys=role_name)
    print(grant_to_role_setting.get())

    print("\nRole IDs to add to group {}: {}".format(role_name, role_ids))

    return role_ids   # returns entire file with edited line, as well as index of current line number


def write_ids(ids_to_write, role_name):
    grant_to_role_setting = config.add_option("GrantToRoles", keys=role_name)
    grant_to_role_setting.set(ids_to_write)  # set key value
    config_file.write(permissions_ini_location)  # write to ini file

    print("Changes written successfully to '{}'".format(os.path.realpath(permissions_ini_location)))
