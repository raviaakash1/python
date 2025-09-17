'''
'''

import yaml
import argparse
import sys

def validate_team_structure(data):
    errors = []

    if "teams" not in data or not isinstance(data["teams"], list):
        errors.append("Missing or invalid 'teams' section.")
        return errors

    for team in data["teams"]:
        team_name = team.get("name", "<Unnamed Team>")
        members = team.get("members", [])

        if not members:
            errors.append(f"Team '{team_name}' has no members.")

        for member in members:
            email = member.get("email", "")
            if not email.endswith("@bmw.de"):
                errors.append(f"Invalid email '{email}' in team '{team_name}'.")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate team structure in YAML.")
    parser.add_argument("yaml_file", help="Path to the YAML file")
    args = parser.parse_args()

    try:
        with open(args.yaml_file, "r") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        sys.exit(1)

    errors = validate_team_structure(data)
    if errors:
        print("❌ Validation Failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Validation Passed!")

if __name__ == "__main__":
    main()