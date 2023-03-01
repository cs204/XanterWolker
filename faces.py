def main():
    e = str(input())
    print(conv(e))


def conv(e):
    if (":)" in e) or (":(" in e):
        e = e.replace(":)", "\N{Slightly Smiling Face}")
        e = e.replace(":(", "\N{Slightly Frowning Face}")

    return e


main()
