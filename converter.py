import csv
import json
import argparse

def csv_to_json(csv_filepath, json_filepath):
    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open(json_filepath, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f'Conversion completed! JSON file saved as {json_filepath}')
    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a CSV file to JSON.')
    parser.add_argument('input', help='Path to the input CSV file')
    parser.add_argument('output', help='Path to the output JSON file')

    args = parser.parse_args()
    csv_to_json(args.input, args.output)
