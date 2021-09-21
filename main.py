from parser import Parser


def main():
    p = Parser()
    pages_amount = p.get_pages_amount()
    print(pages_amount)


if __name__ == '__main__':
    main()
