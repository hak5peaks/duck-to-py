def create_ducky_payload(file_contents):
    ducky_script = """
DELAY 500
"""

    lines = file_contents.split('\n')
    for line in lines:
        ducky_script += f"STRING {line}\nENTER\n"

    return ducky_script

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    python_script_path = "python-script-input.txt" 
    python_script_contents = read_file(python_script_path)

    if python_script_contents.startswith("#!"):
        print("The file appears to be a Python script.")
    else:
        print("Warning: The file may not be a valid Python script. Please ensure it starts with a shebang (#!).")

    ducky_payload = create_ducky_payload(python_script_contents)

    output_file_path = "output.txt"
    try:
        with open(output_file_path, 'w') as output_file:
            output_file.write(ducky_payload)
        print(f"\nDucky Script Payload saved to {output_file_path}")
    except Exception as e:
        print(f"Error writing to {output_file_path}: {str(e)}")

if __name__ == "__main__":
    main()
