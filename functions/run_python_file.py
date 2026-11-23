import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory with optional command-line arguments and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional list of command-line arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file' # ADDED missing 'return'

        command = ["python", target_dir]
        if args is not None and len(args) != 0:
            command.extend(args)

        completed_process = subprocess.run(
            command,
            cwd=working_dir_abs,       # Set the working directory
            capture_output=True,       # Capture stdout and stderr
            text=True,                 # Decode output to strings (not bytes)
            timeout=30                 # Set the 30-second timeout
        )

        # Build the output string
        output_parts = []
        
        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not completed_process.stdout and not completed_process.stderr:
            output_parts.append("No output produced")
        else:
            if completed_process.stdout:
                output_parts.append(f"STDOUT:{completed_process.stdout}")
            if completed_process.stderr:
                output_parts.append(f"STDERR:{completed_process.stderr}")

        return "\n".join(output_parts)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"