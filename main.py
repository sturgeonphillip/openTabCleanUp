import subprocess
import os
from datetime import datetime

# --- ApplesScript gets all open tabs ---
# options: "Brave Browser", "Google Chrome", "Firefox"
BROWSER = "Brave Browser" 
apple_script_template = """
tell application "{browser}"
  set window_list to every window
  set tab_list to ""
  set window_count to 0
  repeat with w in window_list
    set window_count to window_count + 1
    set tab_urls to URL of every tab of w
    set tab_list to tab_list & "Window " & window_count & ":\n"
    repeat with t in tab_urls
      set tab_list to tab_list & t & "\n"
    end repeat
    set tab_list to tab_list & "\n" -- add spacing between windows
  end repeat
  return tab_list
end tell
"""

# --- format AS with chosen browser ---
apple_script = apple_script_template.format(browser=BROWSER)

# --- run AS and capture output ---
result = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)

# --- process tab URLs ---
tab_output = result.stdout.strip()


# --- define output directory and file path ---
project_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(project_dir, "tab_outputs")

# if no directory exists, create one 
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

timestamp = int(datetime.now().timestamp())
output_file = os.path.join(output_dir, f"{BROWSER.replace(' ', '_').lower()}_tabs_{timestamp}.txt")

# save tab URLs grouped by window to file
with open(output_file, "w") as f:
    f.write(tab_output)

# print tabs to console while saving
current_window = None
for line in tab_output.splitlines():
  if line.startswith("Window "):
     current_window = line
     # print window header
     print(f"\n# {line}")
  elif line.startswith("https"):
    # print url
    print(line)


# count total tabs and windows
total_tabs = tab_output.count("https")
total_windows = tab_output.count("Window ")

print(f"\n✅ Saved {total_tabs} tabs from {total_windows} window(s) to '{output_file}'")
