import re

def extract_errors(log_file_path):
    error_pattern = r"\[(.*?)\]\s+ERROR:\s+(CODE_\d+)\s+-\s+(.*)"
    results = []

    with open(log_file_path, "r") as file:
        for line in file:
            match = re.search(error_pattern, line)
            if match:
                timestamp = match.group(1)
                error_code = match.group(2)
                message = match.group(3)
                results.append((timestamp, error_code, message))

    return results

# Example usage
errors = extract_errors("diagnostic.log")
for timestamp, code, message in errors:
    print(f"{timestamp} | {code} | {message}")