# Marysha Brown
# IT-140 final Project
import time

# Set to starting room
current_room = 'Atrium'

# Set inventory list to empty
inventory = []

# Set alien to hidden
alien = 'Hidden'


# Main game function
def main():
    # Dictionary to link rooms, directions, and parts
    main.rooms = {
        'Kitchen': {'South': 'Storage', 'East': 'Cafeteria',
                    'part': '',
                    'information': '- The Alien is here! -'},  # Villain
        'Cafeteria': {'South': 'Library', 'West': 'Kitchen',
                      'part': 'Screen',
                      'information': '- Your stomach rumbles... -',
                      'part information': 'Hmmm... a tablet should work!'},
        'Storage': {'North': 'Kitchen', 'South': 'Cargo Hold / Utility Room',
                    'part': 'Computer Chip',
                    'information': '- Wow! look at all the stuff in here! -',
                    'part information': 'You see a box of old tech parts on a shelf to your right.'},
        'Library': {'North': 'Cafeteria', 'South': 'Atrium', 'East': 'Fitness Center',
                    'part': 'Computer Chip',
                    'information': '- Shhhhhh, people might be studying in here. -',
                    'part information': 'You spy a dusty computer in the far corner.'},
        'Fitness Center': {'South': 'Dormitory', 'West': 'Library',
                           'part': 'Laser Sight',
                           'information': '- No time to workout now! -',
                           'part information': 'You open an equipment storage cabinet.'},
        'Cargo Hold / Utility Room': {'North': 'Storage', 'South': 'Main Control', 'East': 'Atrium',
                                      'part': 'Handle',
                                      'information': '- sick whip -',
                                      'part information': 'You see a flashlight on the workbench on the West wall.'},
        'Atrium': {'North': 'Library', 'South': 'Laboratory', 'East': 'Dormitory', 'West': 'Cargo Hold / Utility Room',
                   'part': '',
                   'information': '- Great lighting and plants. -'},
        'Dormitory': {'North': 'Fitness Center', 'West': 'Atrium',
                      'part': 'Screen',
                      'information': '- Shhh, someone might be sleeping -',
                      'part information': 'Hmmm... a tablet should work!'},
        'Main Control': {'North': 'Cargo Hold / Utility Room',
                         'part': 'Power Source',
                         'information': '- You find Dr. Bozzelli, she says there have been talk of dinner '
                                        'being delayed due to the alien. -',
                         'part information': 'You open a control panel for the AutoSun.'},
        'Laboratory': {'North': 'Atrium',
                       'part': 'Core',
                       'information': '- Important science going on here. -',
                       'part information': 'You look around for a Materials Storage Cabinet.'}
    }

    main.commands = {
        'Direction': ['North', 'South', 'East', 'West'],
        'Exit': ['Quit', 'Exit']
    }
    global alien
    # Loop for gameplay while player searches for all 6 parts.
    while alien == 'Hidden':
        show_status()

        # Loop to losing function if player finds alien.
        if current_room == 'Kitchen':
            jelly_ending()

        player_command = input('What would you like to do? Move or Search: \n'
                               '> ')
        player_command = player_command.title()

        # Player command loop for each action player can do.
        if player_command == 'Move':
            move_rooms()  # Send to move_rooms function.

        elif player_command == 'Search':
            get_parts()  # Send to get_parts function.

        elif player_command == 'Help':
            instructions()  # Prints instructions again.

        elif player_command in main.commands['Exit']:
            print("Thanks for playing!")
            quit()
        else:
            print('You can\'t do that! Try again.')

    # Loop for when player has all 6 parts to win game.
    while alien == 'Unhidden':
        winning_ending()


# Prints intro information
def intro():
    print(
        ' __   __                         _____                                           __      __          _         _____ \n'
        ' \ \ / /                        |  __ \                                          \ \    / /         | |       |_   _|\n'
        '  \ V /    ___   _ __     ___   | |__) |   __ _   _ __     __ _    ___   _ __     \ \  / /    ___   | |         | |  \n'
        '   > <    / _ \ | \'_ \   / _ \  |  _  /   / _` | | \'_ \   / _` |  / _ \ | \'__|     \ \/ /    / _ \  | |         | |  \n'
        '  / . \  |  __/ | | | | | (_) | | | \ \  | (_| | | | | | | (_| | |  __/ | |         \  /    | (_) | | |  _     _| |_ \n'
        ' /_/ \_\  \___| |_| |_|  \___/  |_|  \_\  \__,_| |_| |_|  \__, |  \___| |_|          \/      \___/  |_| (_)   |_____|\n'
        '                                                           __/ |\n'
        '                                                          |___/\n')
    time.sleep(2)
    print('You\'ve been assigned to the exploration base Theta on TOI-540 b.')
    time.sleep(2)
    print('A report states that there have been some indications of other lifeforms targeting the base and '
          'the researchers living there. ')
    time.sleep(2)
    print('This report is a few days old, so you\'re being dispatched to check it out.')
    time.sleep(2)
    print('As a Junior XenoRanger, you\'re excited to prove yourself on your first solo case!\n')
    time.sleep(2)

    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n'
          '_  _  _  _______  _______   _____      ________   _____   _______  _______ ______ \n'
          '|  |  |  |_____|  |_____/  |_____]     |______   |_____]  |______  |______ |     \ \n'
          '|__|__|  |     |  |    \_  |            ______|  |        |______  |______ |_____/ \n'
          '           _______  _____       _______  _____  _____          ______ \n'
          '              |    |     |         |    |     |   |   ___      |_____] \n'
          '              |    |_____|         |    |_____| __|__          |_____] \n'
          '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n')
    time.sleep(2)

    print('You have arrived at base Theta on TOI-540 b.')
    time.sleep(1)
    print('As you taxi into the parking zone on the planet, '
          'your com comes alive with the crew leader, Dr. Bozzelli\'s pleas for help.')
    time.sleep(2)
    print('You\'ve arrived just in time; the alien is in the station and is suspending people in jelly!\n')
    time.sleep(2)


# Prints a main menu and commands.
def instructions():
    print('[Instructions:]\n'
          'You may move through rooms in base Theta using the commands: \'Move\' and \'North\', \'South\', '
          '\'East\', or \'West\'.')
    time.sleep(1)
    print('If you\'d like to exit the game, use the command: \'Exit\'.')
    time.sleep(1)
    print('You can search for parts using the command: \'Search\'')
    time.sleep(1)
    print('Use the command \'Help\' if you need the instructions read to you again.')
    time.sleep(1)
    print('Collect all 6 parts to build the Laser Vertoratio and win!')
    time.sleep(1)
    main()


# Prints status of inventory and current room.
def show_status():
    print('----------------------------------')
    print('You are currently in the {}.'.format(current_room))
    print(main.rooms[current_room]['information'])
    print('▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼')
    print('Your Inventory: {}'.format(inventory))
    print('▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲')


# Function to move between rooms
def move_rooms():
    global current_room
    print('You are currently in the {}.'.format(current_room))
    player_move = input('What direction do you want to move?:\n'
                        '> ')
    player_move = player_move.title()

    # Branch to check if the command entered is a valid direction and to move.
    if player_move in main.commands['Direction']:

        # Branch to move and update the current room player is in.
        if player_move in main.rooms[current_room]:
            current_room = main.rooms[current_room][player_move]
            print()
            print('You move to the {}.'.format(current_room))
            time.sleep(2)
            print()
        else:
            print()
            print('Whoops! Can’t go that way, please try again.')
            time.sleep(2)

    # Branch to end game.
    elif player_move == 'Exit':
        current_room = 'Exit'
        print('Thanks for playing!')
        quit()

    # Branch to get instructions
    elif player_move == 'Help':
        instructions()

    # Branch to output error message of invalid direction.
    else:
        print()
        print("Whoops! That's not even a direction! Please try again.")
        time.sleep(2)
        move_rooms()


# Function to search and add parts to inventory.
def get_parts():
    global current_room
    global alien
    part = main.rooms[current_room]['part']
    if part == '':
        print('...')
        time.sleep(1)
        print('... Searching ...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('You searched but no parts here.')
    else:
        if part not in inventory:
            print('...')
            time.sleep(1)
            print('... Searching ...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print(main.rooms[current_room]['part information'])
            time.sleep(1)
            print('Found a {}!'.format(part))
            time.sleep(1)
            inventory.append(part)
            main.rooms[current_room]['part'] = ''  # Set part value to blank to go to different loop.
            if len(inventory) == 6:
                print('You found all the parts! Time to make the Laser Vertoratio.')
                print('...')
                time.sleep(1)
                print('... a little glue here ...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('... a little tightening there ...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('Done! Let\'s go find the Alien!')
                del inventory[:7]  # Deletes all parts from inventory
                inventory.append('Laser Vertotatio')  # Adds Laser to inventory
                print('New Inventory: {}'.format(inventory))
                alien = 'Unhidden'
        else:
            print()
            print('You already have a similar part, no need to search here.')
            time.sleep(2)


# Ending function if player lost game.
def jelly_ending():
    print('----------------------------------')
    print('Oh no! The You haven’t built the Laser Vertoratio yet.')
    time.sleep(3)
    print('The Alien sees you and spits jelly, hitting you and suspending you in its purple goo.')
    time.sleep(3)
    print('You have failed the mission, XenoRanger.')
    quit()


# Ending function if player won game.
def winning_ending():
    print('Where can the Alien be...')
    # Loop for when player has all 6 parts to win game.
    if current_room == 'Kitchen':
        print('----------------------------------')
        print('You see the Alien on the far side of the room flickering the light switch. \n'
              'Good thing you have built the Laser Vertoratio! Now it’s time to put it to use. \n')
        time.sleep(3)
        print('You turn it on...')
        time.sleep(1)
        print('point it towards the alien...')
        time.sleep(1)
        print('and speak into it “Why are you here?” \n')
        time.sleep(3)
        print('The sound that comes out of the device is like a garbles whale noise that startles the alien. \n')
        time.sleep(3)
        print('It turns towards you and seems to reply! Your screen reads “YOU CAN UNDERSTAND ME”')
        time.sleep(3)
        print('----------------------------------')
        print('You have communicated with the alien to find out it was just curious about what this place was. \n')
        time.sleep(3)
        print('TOI-540 b is its home planet; it was never trying to harm anyone. \n')
        time.sleep(3)
        print('You successfully negotiated the de-jellying of everyone, and diplomatic relations were established '
              'with the Onzons! \n')
        time.sleep(3)
        print('Main Ops is happy, and you might be looking at a promotion soon, XenoRanger!')
        quit()
    else:
        move_rooms()


intro()
instructions()
main()
