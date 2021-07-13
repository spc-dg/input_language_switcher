# input_language_switcher
A minimal script to switch between languages wrote in python. 

A thank you to the autors of these guides:

https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/

https://www.phillipsj.net/posts/executing-powershell-from-python/


The functions to execute are contained in lines similar to this one:


  subprocess.run(["powershell", "-Command", "Set-WinUserLanguageList -Force 'en-US'"])
  

Currently it is configured to execute a powershell command to set up an input language.


The hotkeys are contained in lines similar to this one:


  frozenset([pynput.keyboard.Key.ctrl_l, pynput.keyboard.KeyCode(vk=49)]): function_1,  # LCtrl+1
  

You can edit the combinations using the pynput keyboard documentation located here: https://pynput.readthedocs.io/en/latest/keyboard.html 
Alternatively, you can use virtual key codes instead of key names, you can get vk codes by running the code in vk_listener.
