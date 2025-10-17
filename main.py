import sys
import subprocess
import lexer
from parser import Parser


def transpile_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        rid_code = file.read()

    tokens = lexer.lex(rid_code)

    parser = Parser(tokens)
    parser.parse()

    python_code = '\n'.join(parser.output)

    with open(output_filename, 'w') as file:
        file.write(python_code)

    print(f"Transpiled {input_filename} to {output_filename}")

    return output_filename


def run_python_file(filename):
    print(f"\nRunning {filename}...\n")
    print("=" * 40)
    result = subprocess.run(['python', filename], capture_output=False)
    print("=" * 40)
    return result.returncode


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input.rid> [output.py]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.py"

    output_filename = transpile_file(input_file, output_file)

    exit_code = run_python_file(output_filename)

    sys.exit(exit_code)