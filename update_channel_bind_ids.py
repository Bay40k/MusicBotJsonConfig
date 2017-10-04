import json
import os
import cfgparse  # used to edit ini in place without modifying things like comments

json_id_list_location = 'channel_bind_ids.json'  # binds json, where Channel Label/ID pair Json is located
options_ini_location = 'options.ini'  # options.ini location for music

config = cfgparse.ConfigParser()  # add parser
config_file = config.add_file(options_ini_location)  # add ini file

bind_setting = config.add_option("BindToChannels", keys="Chat")  # define which setting to change


def main():
    write_ids(print_ids(get_channel_ids()))
    return


def get_channel_ids():
    with open(json_id_list_location) as json_binds_list:
        binds_json = json.load(json_binds_list)

    channel_ids = []

    print("\nJson File: {}".format(os.path.realpath(json_id_list_location)))
    print("Label : Channel ID\n")

    channel_id_table = binds_json["channelIDs"]
    for key in channel_id_table:
        value = channel_id_table[key]
        print(key + " : " + value)
        channel_ids.append(value)

    channel_ids = " ".join(channel_ids)

    return channel_ids  # returns just our IDs, separated by space


def print_ids(channel_ids):
    print("\nFile: '{}'".format(os.path.realpath(options_ini_location)))
    print("Existing IDs")

    print(bind_setting.get())  # print existing setting

    print("\nChannel IDs to add: {}".format(channel_ids))

    return channel_ids  # returns channel IDs to add


def write_ids(ids_to_write):
    bind_setting.set(" " + ids_to_write)  # set key value
    config_file.write(options_ini_location)  # write to ini file

    print("Changes written successfully to '{}'".format(os.path.realpath(options_ini_location)))
