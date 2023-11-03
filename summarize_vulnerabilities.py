
import json
import sys

def summarize_vulnerabilities(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to count vulnerabilities by severity
    vulnerabilities_summary = {
        'UNKNOWN': 0,
        'LOW': 0,
        'MEDIUM': 0,
        'HIGH': 0,
        'CRITICAL': 0
    }

    # Recursive function to find the vulnerabilities in the data
    def find_vulnerabilities(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'Vulnerabilities':
                    for vulnerability in value:
                        severity = vulnerability.get('Severity', 'UNKNOWN').upper()
                        vulnerabilities_summary[severity] += 1
                else:
                    find_vulnerabilities(value)
        elif isinstance(data, list):
            for item in data:
                find_vulnerabilities(item)

    # Find the vulnerabilities and count them by severity
    find_vulnerabilities(data)

    # Print the summary
    for severity, count in vulnerabilities_summary.items():
        print(f'{severity}: {count}')

# Replace 'path_to_results.json' with the actual path to your Trivy scan JSON file
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python summarize_vulnerabilities.py <path_to_trivy_results.json>")
        sys.exit(1)

    results_file_path = sys.argv[1]
    summarize_vulnerabilities(results_file_path)
