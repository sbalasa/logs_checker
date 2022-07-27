import os
import json


def main():
    """
    Main function to check if the errors from errors.json are present in log files
    from logs folder respectively.
    """
    with open("error.json", "r") as f:
        errors = json.load(f)
    for idx, error in errors.items():
        for log in os.listdir("./logs"):
            with open("./logs/" + log, "r") as lf:
                if any(error in content for content in lf.readlines()):
                    print(f"{idx} is present in {log}")
                else:
                    print(f"{idx} is not present in {log}")


if __name__ == "__main__":
    main()
