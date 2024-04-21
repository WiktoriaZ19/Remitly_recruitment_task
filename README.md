# Verifying the input JSON data


## General Information
The check_json.py script is a tool for validating the structure of JSON files containing policies. Input data format is defined as AWS::IAM::Role Policy.


## Requirements
- Python 3.11
- Modeule json
- Module re


## Running instructions

### Execution
1. Download the check_json.py file to your computer.
2. To run the script:
`python check_json.py`
3. After running the script, it will prompt you for the path to the JSON file which you want to check.

### Testing
1. Download the test_json.py file and '*.json' and '*.txt' testing files to your computer.
2. To run the test script:
`python -m unittest check_json.py`
