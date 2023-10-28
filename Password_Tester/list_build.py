import argparse,itertools,sys
from itertools import product


def test():
    date = [1,2,3]
    for data_path in product(date,repeat=2):
        print(data_path)

def arg_parse():
    try:
       arg = argparse.ArgumentParser(description="")
       arg.add_argument("-word",nargs="*",default="",help="")
       arg.add_argument("-line",default=3,help="")
       arg.add_argument("-file",type=str,default="password",help="")
       parser = arg.parse_args()
       list_build(parser.word,parser.line,parser.file)
    except TypeError:
        sys.stdout.write("\nHelp_Command -h , --help")
        sys.exit()


def list_build(word_list,line_data,file_name,cycle=itertools.cycle(r"/-\|")):

    for date in product(word_list,repeat=int(line_data)):
        with open(f"{file_name}.txt","a+",encoding="utf-8")as password:
            password_data = "".join(date)

            sys.stdout.write("\r")
            sys.stdout.write(f"Builds-Password -> {password_data} ~ {next(cycle)}")
            sys.stdout.flush()

            password.write(f"{password_data}\n")
    return f"{file_name}.txt"


if __name__ == "__main__":
    arg_parse()





