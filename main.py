from Tools import cli


def main():
    command = cli.CLI()
    command.check_args()
    command.execute()


if __name__ == "__main__":
    main()