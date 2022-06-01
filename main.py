import argparse

from modules.tester import Tester

parser = argparse.ArgumentParser()
parser.add_argument('--automatic', action='store_true')
parser.add_argument('--manual', dest='automatic', action='store_false')
parser.set_defaults(feature=True)

if __name__ == "__main__":
    args = parser.parse_args()
    automatic = args.automatic is True
    Tester().run(automatic=automatic)
