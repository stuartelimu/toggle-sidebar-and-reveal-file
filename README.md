# toggle-sidebar-and-reveal-file
A Sublime Text 3 plugin to toggle sidebar and reveal current file

## Installation

1. Using Package Control, install "Clipboard Manager"
2. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

You need to override the toggle sidebar command. Open `Preferences > Key Bindings` and add this snippet

```
{ "keys": ["super+k", "super+b"], "command": "toggle_sidebar_and_reveal_file" },
```

## Usage

`super+k, super+b` : toggle and reveal current file in the sidebar. 

### Note
- If it's a new window, nothing happens
- If the sidebar is open, and the current file is already reveal, it will simply close the sidebar

## Contribute

You can always send a pull request or create an issue.