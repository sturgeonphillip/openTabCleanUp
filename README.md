# Open Tab Clean Up

A Python and AppleScript script to save the URL of all open tabs at the current time into a text file.

Sometimes you don't want to sort through all your open windows or bookmark every open tab.
Take those half-read articles, products you're on the fence about, and all the other clutter.
Sweep it all under the metaphorical rug. Great for hoarders who aren't sure if they'll want to revisit a link but can't bring themselves to close it.

Tabs are grouped by window, saved in a timestamped text document.

File is save as {browser}_tabs_{datetime.now()} into openTabCleanUp/tab_outputs

Example:
Running the script at 12:35:37 on March 24, 2025 saves all of your open tabs to
`openTabCleanUp/tab_outputs/brave_browser_tabs_1742844938145.txt`

See the included screenshots in ./screenshots and the included text file in ./tab_outputs/brave_browser_tabs_1742842772.txt

To run:

```cli
git clone https://github.com/sturgeonphillip/openTabCleanUp

cd openTabCleanUp
```

Edit `main.py` to set the BROWSER variable to your browser.

`BROWSER = "Brave Browser"`

Save the file and run it.

```cli
python3 main.py
```



TO DO:
- Test and run on other browsers.
- Modify so that when script is run it prompts user to enter browser as input so there's no need to modify `main.py`
- Write a follow-up prompt that asks if it should close all current tabs and windows after writing output to file.
- Incorporate screenshots into `README.md` and remove example output.
