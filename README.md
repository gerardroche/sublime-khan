# Khan

Add, remove, and clear rulers at the current cursor using the command palette.

## Usage

**Add a ruler**

Put your cursor at the column where you want a ruler and run "Add Ruler" from the command palette.

Command Palette → Khan: Add Ruler

**Remove a ruler**

Put your cursor at the ruler you want to remove and run "Remove Ruler" from the command palette.

Command Palette → Khan: Remove Ruler

**Clear rulers**

Run "Clear Rulers" from the command palette.

Command Palette → Khan: Clear Rulers

## Installation

**Method 1: Using Package Control**

1. Open Sublime Text.
2. Access the Command Palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "Khan" and select it from the list of available packages.

**Method 2: Manual Installation**

1. Visit the [Khan GitHub repository](https://github.com/gerardroche/sublime-khan).
2. Click on the "Code" button and choose "Download ZIP."
3. Unzip the downloaded file.
4. In Sublime Text, navigate to `Preferences -> Browse Packages...` to access the Packages folder.
5. Copy the "Khan" folder from the unzipped archive and paste it into the Packages folder.

**Method 3: Manual Git Repository Installation**

1. Open a terminal or command prompt.
2. Go to the Sublime Text Packages directory based on your operating system:
   - Windows: `%APPDATA%\Sublime Text\Packages`
   - macOS: `~/Library/Application Support/Sublime Text/Packages`
   - Linux: `~/.config/sublime-text/Packages`
3. Clone the Khan plugin repository directly into the Packages directory using Git:

   ```bash
   git clone https://github.com/gerardroche/sublime-khan.git Khan
   ```

## Commands

Command             | Description
:------             | :----------
Khan: Add Ruler     | Add a ruler at the current column
Khan: Clear Rulers  | Clear all rulers
Khan: Remote Ruler  | Remove the ruler at the current column

## License

Released under the [GPL-3.0-or-later License](LICENSE).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
