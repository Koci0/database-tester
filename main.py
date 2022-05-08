import argparse

from modules.tester import Tester

parser = argparse.ArgumentParser()
parser.add_argument("--automatic", choices=["True", "False"], default="True",
                    help="Runs automatically if True, waits for user input after each section if False")

if __name__ == "__main__":
    args = parser.parse_args()
    automatic = bool(args.automatic) is True
    Tester().run(automatic=automatic)
