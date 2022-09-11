import argparse
import os
from model import NgrammModel

def main():
    parser = argparse.ArgumentParser(description='ngramm-Model')
    parser.add_argument("--input-dir", help="Input directory")
    parser.add_argument("--model", help="Model filename")
    parser.add_argument("--n", nargs='?', help="Choose n in ngramm-model", default=5)
    args = parser.parse_args()
    with NgrammModel(model_filename=args.model) as model:
        for filename in os.listdir(args.input_dir):
            processed, err = model.fit(args.input_dir + "/" + filename, int(args.n))
            if processed:
                print(filename, "processed")
            else:
                print(err)


if __name__ == '__main__':
    main()