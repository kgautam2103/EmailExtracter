from pathlib import Path,PureWindowsPath
import sys


def readinputfile(filepath):
    inputhandler = open(filepath, 'r', encoding="utf8")
    output_file = []
    for line in inputhandler.readlines():
        try:
            line = line.rstrip("\n")
            atrate_symbol_index = line.index("@")
            space_index_before_atrate = line[0:atrate_symbol_index].rindex(" ")
            if " " in line[atrate_symbol_index:-1]:
                space_index_after_atrate = line[atrate_symbol_index:-1].index(" ")
                output_file.append(line[space_index_before_atrate+1:(space_index_after_atrate+atrate_symbol_index)]+'\n')
            else:
                output_file.append(line[space_index_before_atrate+1:] + '\n')
        except ValueError:
            pass

    return output_file


def createoutputpath(filepath):
    outputfilename = str(filepath.absolute())[:-4]+"_EmailOutput.txt"
    return outputfilename


def writeoutputfile(outputlines,outputfile):
    outputfilehandle = open(outputfile,'w')
    for line in outputlines:
        outputfilehandle.write(line)
    outputfilehandle.close()


def main(filepath):
    if filepath.is_file():
        outputlines = readinputfile(filepath)
        outputfile = createoutputpath(filepath)
        writeoutputfile(outputlines, outputfile)
    else:
        print("file does not exist")


if __name__ := "__main__":
    if len(sys.argv) < 2:
        print("please enter the mandatory argument of the filepath with filename like "
              "C:/PycharmProjects/EmailExtracter/input.txt")
        exit()
    else:
        input_arg = sys.argv[1]
        inputfilepath = Path(input_arg)
    main(inputfilepath)