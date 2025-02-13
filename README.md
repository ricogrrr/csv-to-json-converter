📌 CSV to JSON Converter

This Python script converts a CSV file into a JSON file using built-in modules.

🚀 Features

Reads data from a CSV file.

Converts the data into JSON format.

Saves the output as a formatted JSON file.

🔧 Requirements

Ensure you have Python 3.x installed. No additional libraries are required as the script uses built-in modules.

📄 Usage

Place your CSV file in the same directory as the script.

Update the script with your input CSV filename and desired output JSON filename.

Run the script.

The converted JSON file will be saved in the same directory.

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