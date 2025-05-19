print("[DEBUG] Script started")
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import traceback

try:
    # Initialize Airtest environment
    if not cli_setup():
        print("[DEBUG] Running auto_setup and connecting to Windows desktop device")
        auto_setup(__file__, devices=["Windows:///"], logdir=True)

    # Print the current device after auto_setup
    current_dev = device()
    print(f"[DEBUG] Current device: {current_dev}")

    # Start Notepad first
    print("[DEBUG] Starting Notepad")
    start_app("notepad.exe")
    sleep(2)  # Wait for Notepad to open

    # Type text using keyevent instead of text()
    print("[DEBUG] Typing 'hello world!' using keyevent")
    keyevent("h")
    keyevent("e")
    keyevent("l")
    keyevent("l")
    keyevent("o")
    keyevent(" ")
    keyevent("w")
    keyevent("o")
    keyevent("r")
    keyevent("l")
    keyevent("d")
    keyevent("!")
    
    # Click on the homebutton icon using image recognition
    print("[DEBUG] Clicking on homebutton icon")
    touch(Template("homebutton.png"))

    # Click on the searchbar icon using image recognition
    print("[DEBUG] Clicking on searchbar icon")
    touch(Template("searchbar.png"))

    # Type 'hello world!' again in the searchbar
    print("[DEBUG] Typing 'hello world!' in the searchbar")
    keyevent("h")
    keyevent("e")
    keyevent("l")
    keyevent("l")
    keyevent("o")
    keyevent(" ")
    keyevent("w")
    keyevent("o")
    keyevent("r")
    keyevent("l")
    keyevent("d")
    keyevent("!")
    
    # Take a screenshot for verification
    snapshot("notepad_result.png", msg="Screenshot after typing")
    
    print("[DEBUG] Script finished successfully")
except Exception as e:
    print(f"[ERROR] {e}")
    traceback.print_exc() 
