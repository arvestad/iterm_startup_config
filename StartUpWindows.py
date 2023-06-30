#!/usr/bin/env python3.7

import iterm2
import json
import os


setup_file = '.iterm2_user_setup.json'


def user_file(filename):
    username = os.getenv('USER')
    path = os.path.expanduser(f'~{username}')
    return f'{path}/{filename}'


# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    # Your code goes here. Here's a bit of example code that adds a tab to the current window:
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is None:
        # You can view this message in the script console.
        print("No current window")
    else:
        filename = user_file(setup_file)
        with open(filename) as h:
            user_setup = json.load(h)

        for title, directory in user_setup:
            window = await iterm2.Window.async_create(connection)

            tab = app.current_terminal_window.current_tab
            session = tab.current_session
            await session.async_send_text(f'cd {directory}\n')
            await session.async_set_name(title)
#            await session.async_send_text(f'title {title}\n')

            await tab.async_set_title(title)
    
iterm2.run_until_complete(main)
