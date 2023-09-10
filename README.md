
# 🐕 ScrapPY: Advanced, User-Friendly PDF Analysis for Cybersecurity

![ScrapPY Banner](banner.png)

ScrapPY is an innovative and comprehensive Python utility, designed to scan PDF files such as manuals, documents, and other sensitive materials. This utility generates targeted wordlists, which can be used in a variety of cybersecurity applications like brute force attacks, forced browsing, and dictionary attacks. Unlike its predecessor, [www-project-scrappy](https://github.com/OWASP/www-project-scrappy), this fork is designed for maximum user-friendliness, offering a graphical interface, multilingual support, faster performance through concurrent page reading, extensive logging, and more.

## 📑 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Progress](#-progress)
- [Output](#-output)
- [Integration with Other Tools](#-integration-with-other-tools)
- [Future Development](#-future-development)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features
### Intuitive User Interface
- **Zero Command-Line Requirement**: Designed with accessibility in mind. Anyone can use it; no need to navigate through the command line.
- **Multilingual Support**: Localize the application with language-specific JSON files.
  
### Advanced Analysis Modes
- **Multiple Modes of Operation**: Includes 'word-frequency', 'full', 'metadata', and 'entropy' modes.
  
### Performance
- **Concurrent Page Reading**: Utilizes multithreading for data extraction, significantly speeding up the process.

### Robust Logging
- **Extensive Logging**: Keeps track of events and errors in `ScrapPY.log`.

### Customization
- **Custom Output**: Allows users to specify the name of the output file.

## 💽 Installation

1. **Clone the Repository**:

    ```
    mkdir MyScrapPY
    cd MyScrapPY/
    git clone https://github.com/Xeo-V/ScrapPY.git
    ```
2. **Install Dependencies**:

    ```
    pip3 install -r requirements.txt
    ```

## 🛠 Usage
Run the script to interactively select the language and operation mode.
```bash
python3 MyScrapPY.py
```

### 🚀 Modes of Operation
- `word-frequency`: Outputs the 100 most frequently used keywords.
- `full`: Outputs all unique keywords.
- `metadata`: Outputs PDF metadata like title, author, etc.
- `entropy`: Outputs the 100 keywords with the highest entropy rating.

## 📊 Progress

The program features an ASCII progress bar to give you real-time updates on its operation.

```
[====================100====================]
```

## 🗂 Output
The tool generates a text file, either with a default name of `ScrapPY.txt` or a name specified by the user.

### File Commands
- **View the first 50 lines**:

    ```
    head -50 MyScrapPY.txt
    ```
- **Check the word count**:

    ```
    wc -l MyScrapPY.txt
    ```

## 🛠 Integration with Other Tools
- **Dirb**:

    ```
    dirb http://192.168.1.123/ /path/to/MyScrapPY.txt
    ```
- **Hydra**:

    ```
    hydra -l root -P /path/to/MyScrapPY.txt -t 6 ssh://192.168.1.123
    ```
- **Nmap**:

    ```
    nmap -p445 --script smb-brute.nse --script-args userdb=users.txt,passdb=MyScrapPY.txt 192.168.1.123
    ```

## 🌟 Future Development
- OCR support to extract data from images in PDFs.
- Add a command-line interface as an alternative.
- Enhance metadata analysis capabilities.
- Implement unit tests for better code maintainability.

## 👩‍💻 Contributing
Feel free to open issues or PRs for additional features, bug fixes, or other types of contributions. Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 📄 License
MIT License. See `LICENSE` for more information.

---

