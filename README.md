# VAN Card Reformatter

VAN Card Reformatter is a python script for taking PDFs of Member cards from VAN and reformatting them to fit on multiple 8.5 x 11 pages

## Description
When downloading PDF documents from VAN, typically the result is a printscreen dependent on the device's size. This reformats the printscreen PDF to either shrink or expand to make accessible to 8.5x11 pages. The primary use case is to send to employers for them to keep for this records, however this can also be used for internal storage purposes. 

# Getting Started

## Dependancies
- Python 3.10.12
- Packages: [glob](https://docs.python.org/3/library/glob.html), [https://docs.python.org/3/library/subprocess.html](subprocess), [os](https://docs.python.org/3/library/os.html), [PyPdf2](https://pypi.org/project/PyPDF2/)

## Installation and Usage

Download python script and place in seperate folder on system. Then run via bash terminal or equivalent:

```bash
python VanCardConvert.py
```
This will generate two additional folders on first use. Place cards you want to convert in "Original_Cards" and run again. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

 This work is licensed under (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International)[https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1] 
