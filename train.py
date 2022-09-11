import argparse
import os

from model import BigramModel


def main():
    parser = argparse.ArgumentParser(description='Big-ramModel')
    parser.add_argument("--input-dir", help="Input directory")
    parser.add_argument("--model", nargs='?', help="JOPA Model")
    args = parser.parse_args()

    with BigramModel(model_filename=args.model) as model:
        for filename in os.listdir(args.input_dir):
            processed, err = model.fit(args.input_dir + "/" + filename)
            if processed:
                print(filename, "processed")
            else:
                print(err)


if __name__ == '__main__':
    main()