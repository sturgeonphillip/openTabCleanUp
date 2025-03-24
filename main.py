import subprocess
import os
from datetime import datetime

# --- ApplesScript gets all open tabs ---
# options: "Brave Browser", "Google Chrome", "Firefox"
BROWSER = "Brave Browser" 
apple_script_template = """
tell application "{browser}"
  set window_list to every window
  set tab_list to {{}}
  repeat with w in window_list
    set tab_urls to URL of every tab of w
    set tab_list to tab_list & tab_urls
  end repeat
  return tab_list
end tell
"""

# --- format AS with chosen browser ---
apple_script = apple_script_template.format(browser=BROWSER)

# --- run AS and capture output ---
result = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)

# --- process tab URLs ---
tab_urls = [url.strip() for url in result.stdout.strip().split(",") if url.strip()]

# --- define output directory and file path ---
project_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(project_dir, "tab_outputs")

# if no directory exists, create one 
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

timestamp = int(datetime.now().timestamp())
output_file = os.path.join(output_dir, f"{BROWSER.replace(' ', '_').lower()}_tabs_{timestamp}.txt")

# --- save tab URLs to file path ---
with open(output_file, "w") as f:
  for url in tab_urls:
    f.write(url + "\n")

print(f"✅ Saved {len(tab_urls)} tabs to '{output_file}'")
