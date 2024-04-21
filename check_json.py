import json
import re


def check_json_data(f_path):
    try:
        with open(f_path, 'r') as f:
            j = json.load(f)

            if not isinstance(j, dict):
                raise ValueError("File must be a JSON object.")

            if "PolicyName" not in j:
                raise ValueError("PolicyName is missing.")

            if "PolicyDocument" not in j:
                raise ValueError("PolicyDocument is missing.")

            policy_document = j["PolicyDocument"]

            if not isinstance(policy_document, dict):
                raise ValueError("PolicyDocument must be a JSON object")

            if "Version" not in policy_document:
                raise ValueError("Version is missing in PolicyDocument.")

            if "Statement" not in policy_document:
                raise ValueError("Statement is missing in PolicyDocument.")

            statement = policy_document["Statement"]

            if not isinstance(statement, list):
                raise ValueError("Statement must be a list")

            for stat in statement:
                if not isinstance(stat, dict):
                    raise ValueError("Each statement must be a JSON object")

                if "Resource" not in stat:
                    raise ValueError("Each statement must consist Resource")

                resource = stat["Resource"]

                if not isinstance(resource, str):
                    raise ValueError("Resource must be a string.")

                pattern = r"^\*$"
                return not bool(re.search(pattern, resource))

    except FileNotFoundError:
        print("File not found")


def result():
    path = input("Path to the JSON file: ")
    res = check_json_data(path)
    print(res)


if __name__ == "__main__":
    result()