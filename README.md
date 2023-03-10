## Code Generator 👻

This is a simple Flask web application that generates random codes of a given length and type (either numerical or alphanumeric). The generated codes are saved to a text file in the output directory with a timestamped filename.

### Installation

1. Clone this repository: git clone https://github.com/snowhaystack/ccg.git
2. Install the required packages: `bash pip install -r requirements.txt`

### Usage

1. Run the Flask app: `bash python app.py`
2. Navigate to http://localhost:5000 in your web browser.
3. Fill out the form with the desired code type (numerical or alphanumeric), code length, and number of codes to generate.
4. Click the "Generate Codes" button.
   The generated codes will be saved to a text file in the output directory.
   A message will be displayed on the webpage indicating the number of codes generated and the filename of the output file.

### Dependencies

The project's dependencies are listed in the requirements.txt file.
To install them, run:

```bash
pip install -r requirements.txt
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.
