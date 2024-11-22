import tabulate


class Main:

    def main(self):
        design = [
            ["1", "Register"],
            ["2", "Longin"],
            ["0", "Exit"]
        ]
        print(tabulate.tabulate(design, tablefmt="mixed_outline"))
        key = input(">>> ")
        match key:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
