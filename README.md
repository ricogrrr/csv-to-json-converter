📌 CSV to JSON Converter

This Python script converts a CSV file into a JSON file using built-in modules.

🚀 Features

- Reads data from a CSV file.
- Converts the data into JSON format.
- Saves the output as a formatted JSON file.
- Command-line interface for easy usage.
- Error handling for file operations.

🔧 Requirements

Ensure you have Python 3.x installed. No additional libraries are required as the script uses built-in modules.

📄 Usage

Run the script from the command line by providing the input CSV file path and the desired output JSON file path.

```bash
python3 converter.py <input_csv_file> <output_json_file>
```

Example:
```bash
python3 converter.py Users.csv Test.json
```

The converted JSON file will be saved at the specified output path.

📝 Example

Input (Users.csv):

name,age,email
Alice,25,alice@example.com
Bob,30,bob@example.com

Output (Test.json):

[
    {
        "name": "Alice",
        "age": "25",
        "email": "alice@example.com"
    },
    {
        "name": "Bob",
        "age": "30",
        "email": "bob@example.com"
    }
]
