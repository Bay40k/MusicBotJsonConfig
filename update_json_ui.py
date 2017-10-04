import json
import update_channel_bind_ids
import update_group_role_ids
from update_json import add_key_value_pair
from update_json import remove_key_value_pair

channel_id_json = "channel_bind_ids.json"
role_id_json = "role_ids.json"


def ui():
    available_commands = "Available Commands:\n\n1 = Add Channel to Bind List\n2 = Add role to group\n" \
                         "3 = Write JSON to config\n4 = Delete Channel from bind list\n" \
                         "5 = Delete role ID from group\n9 = Exit"
    print(available_commands)

    def yes_or_no(prompt):
        while True:
            user_input = raw_input(prompt + "\nEnter y or n")
            user_input = user_input.strip().lower()
            if user_input == "y":
                return 0
            elif user_input == "n":
                return 1
            else:
                print("Invalid answer. y or n only.")

    def check_if_group_exists(group_name):
        with open(role_id_json) as json_binds_list:
            binds_json = json.load(json_binds_list)

        for key in binds_json:
            if key == group_name:
                return True

    while True:
        user_input = raw_input("\nChoose a number: ")
        user_input = user_input.strip().lower()

        if user_input == "1":
            channel_label = raw_input("Enter arbitrary Channel Label\n")
            channel_id = raw_input("Enter Channel ID\n")
            if yes_or_no("\nIs this correct?\nLabel: {}\nID: {}".format(channel_label, channel_id)) == 0:
                add_key_value_pair("channelIDs", channel_label, channel_id, channel_id_json)

        elif user_input == "2":
            group_name = raw_input("Enter group name to add ID to\n")
            channel_label = raw_input("Enter arbitrary Role Label\n")
            channel_id = raw_input("Enter Role ID\n")

            if yes_or_no("\nIs this correct?\nLabel: {}\nID: {}".format(channel_label, channel_id)) == 0:
                if check_if_group_exists(group_name):
                    add_key_value_pair(group_name, channel_label, channel_id, role_id_json)
                else:
                    print("Invalid group name '{}'".format(group_name))
                    with open(role_id_json) as json_binds_list:
                        binds_json = json.load(json_binds_list)
                    print("\nAvailable groups:")
                    for key in binds_json:
                        print(key)
                    return
        elif user_input == "3":
            update_channel_bind_ids.main()
            update_group_role_ids.main()

        elif user_input == "4":
            print("Valid labels:")
            with open(channel_id_json) as json_binds_list:
                binds_json = json.load(json_binds_list)

            role_id_table = binds_json["channelIDs"]
            for key in role_id_table:
                print(key)

            channel_label = raw_input("Enter label to delete\n")
            if yes_or_no("\nIs this correct?\nLabel: {}".format(channel_label)) == 0:
                channel_label = channel_label.strip()
                try:
                    remove_key_value_pair("channelIDs", channel_label, channel_id_json)
                except KeyError:
                    print("KeyError, the channel label was probably invalid.")

        elif user_input == "5":
            group_name = raw_input("Enter group name to delete ID from (exact match)\n")
            if check_if_group_exists(group_name):
                print("Valid labels:")
                with open(role_id_json) as json_role_list:
                    binds_json = json.load(json_role_list)

                role_id_table = binds_json[group_name]
                for key in role_id_table:
                    print(key)

                channel_label = raw_input("Enter Role Label to delete (exact match)\n")
                channel_label = channel_label.strip()

                if yes_or_no("\nIs this correct?\nLabel: {}".format(channel_label)) == 0:
                    try:
                        remove_key_value_pair(group_name, channel_label, role_id_json)
                    except KeyError:
                        print("KeyError, the label was probably invalid.")
            else:
                print("Invalid group name '{}'".format(group_name))
                with open(role_id_json) as json_role_list:
                    binds_json = json.load(json_role_list)
                print("\nAvailable groups:")
                for key in binds_json:  # print group keys
                    print(key)

        elif user_input == "9":
            return

        else:
            print("\n'{}' is not a valid number.".format(user_input))
            print(available_commands)


ui()
