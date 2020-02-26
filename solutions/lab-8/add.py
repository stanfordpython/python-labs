def add_all(arguments):
    total = 0.0
    for item in arguments:
        try:
            total += float(item)
        except ValueError:  # Item was non-numeric
            pass
    return total

def help():
    return """Usage: python3 add.py <nums>
    Add some numbers together."""

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # Ignore the executable name
    if not arguments:
        print(help())
        sys.exit(1)
    print(add_all(arguments))
