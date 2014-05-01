# parse.py - Performs constituency and dependency parsing on a sentence using the Stanford parser


def parse(sentence="", folder="parser"):
    """ Accepts a sentence to parse and optionally the folder where the stanford parser is located (default 'parser')
        Returns a tuple containing the constituency parse and dependency parse
    """

    if sentence != "":
        # If sentence is given, put it in the file test.txt and then run parse_file()
        writefile = open("readlines.txt", "w")
        writefile.write(sentence)
        writefile.close()

    return parse_file("readlines.txt", folder)

def parse_file(filepath, folder="parser"):
    """ Accepts a file path to parse and optionally the folder where the stanford parser is located (default 'parser')
    	Returns a tuple containing the constituency parse and dependency parse
    """

    import os    # Needs migration to subprocess

    parser_output = os.popen(folder + '/lexparser.sh "' + filepath + '"').read()
    parser_output = parser_output.split("\n\n")

    return parser_output[0], parser_output[1]

# Driver function

if __name__ == "__main__":
	parsed_output = parse(sentence)
