# RTLO-Detector
Find potentially malicious files by checking for RTLO (Right to Left Override) characters

New types of phishing attacks are always onthe rise and a new form of malicious software will mask the true file extension by using RTLO characters. These will ask the OS to flip the order of the filename when it is being displayed


This is a simple Python script that helps detect malicious files that hide their true filenames using Unicode Right-to-Left Override (RTLO) characters. It will do htis by recursively searching the specified directory and compare the filenames with those on the backlist. a file match with the blacklist does not guarantee that it is malicious. It is just an indicator that the file should be further investigated.


## Usage

1. Clone the repository to your local machine using `git clone https://github.com/sakgoyal/RTLO-Detector.git`
2. Open a terminal and navigate to the directory containing the cloned repository.
3. Run the Python script using the following command: 

`NOTE: Please specify the full path to the directory you want to search or else it may not work as expected.`

```python
python3 detect_filenames.py /path/to/directory1 /path/to/directory2 ...
```
The script will prompt you to enter the search location if you do not provide them.
## Requirements

This script requires Python 3.x and the `glob` and `os` libraries.

## Contributing

If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the GPLv2 License. See the [LICENSE](LICENSE) file for details.
