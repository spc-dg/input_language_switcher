import pynput.keyboard

import subprocess

def function_1():
    # One of the  functions to be executed by a combination
    subprocess.run(["powershell", "-Command", "Set-WinUserLanguageList -Force 'en-US'"])

def function_2():
    subprocess.run(["powershell", "-Command", "Set-WinUserLanguageList -Force 'ru-RU'"])

def function_3():
    subprocess.run(["powershell", "-Command", "Set-WinUserLanguageList -Force 'de-DE'"])

combination_to_function = {
    frozenset([pynput.keyboard.Key.ctrl_l, pynput.keyboard.KeyCode(vk=49)]): function_1,  # LCtrl+1
    frozenset([pynput.keyboard.Key.ctrl_l, pynput.keyboard.KeyCode(vk=50)]): function_2,  # LCtrl+2
    frozenset([pynput.keyboard.Key.ctrl_l, pynput.keyboard.KeyCode(vk=51)]): function_3,  # LCtrl+3
}

pressed_vks = set()


def get_vk(key):
    # Get the virtual key code from a key.
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    # Match the pressed keys against a combination
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    # When a key is pressed
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in combination_to_function:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            combination_to_function[combination]()  # If so, execute the function


def on_release(key):
    # When a key is released
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
