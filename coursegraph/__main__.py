import argparse
import sys

import fontutil
from show_table import ShowTable
from show_graph import read_subjects, draw_course_structure


def main():
    try:

        parser = argparse.ArgumentParser(
            description='A CLI utility for processing data.',
            epilog='Enjoy using the CLI utility!'
        )

        # Adding command line options
        parser.add_argument('-i', '--input', required=True, type=str, help='Specify the input YAML data file path.')
        parser.add_argument('-o', '--output', type=str, help='Specify the output image file path.')
        parser.add_argument('-f', '--format', choices=['graph', 'table'], default='graph', help='Specify the output format (graph, table). Defaults to graph.')
        parser.add_argument('-s', '--size', type=str, help='Specify the size of the output image in format WIDTHxHEIGHT. Example: -s 800x600')

        args = parser.parse_args()

        # Additional validation
        if args.size:
            try:
                width, height = map(int, args.size.split('x'))
            except ValueError:
                parser.error("Size must be in the format WIDTHxHEIGHT. Example: -s 800x600")
        else:
            width, height = 20, 

        # Accessing the command line options
        input_file = args.input
        output_file = args.output
        output_format = args.format
        show_mode = False
        # Perform actions based on options

        if args.size:
            width, height = map(int, args.size.split(','))
        else:
            # Default size
            width, height = 20,10

        if output_file:
            print(f"The output image file path has been specified: {output_file}")
        else:
            show_mode = True

        if input_file:
            print(f"The input YAML file path has been specified: {input_file}")
        else:
            parser.print_help(sys.stderr)
            raise Exception("input file not specified")
        if output_format == 'graph':
            subjects = read_subjects(input_file)
            draw_course_structure(subjects, output_file,width,height)
        elif output_format == 'table':
            # kyahnu: 이 부분 --input 과 --output 을 활용하도록 일관된 인터페이스로 수정할 것
            data_processor = ShowTable(not show_mode, input_file, output_file,width,height)
            data_processor.process_data()
        else:
            raise Exception(f"cannot handle output format {output_format}")


    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    # Add more functionality based on your application needs


if __name__ == '__main__':
    main()
