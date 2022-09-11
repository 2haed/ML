import argparse
from train import BigramModel



def main():
    parser = argparse.ArgumentParser(description='Big-ramModel')
    parser.add_argument("--model", help="model filename")
    parser.add_argument("--length", help="length of output generated text")
    parser.add_argument("--prefix", nargs='?', help="beginning of the text")
    args = parser.parse_args()
    with BigramModel(model_filename=args.model) as model:
        for s in model.generate(int(args.length), args.prefix):
            print(s)

if __name__ == '__main__':
    main()