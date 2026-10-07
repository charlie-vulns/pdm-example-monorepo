from tempfile import mktemp


def write_demo_result(result: str) -> str:
    filename = mktemp()
    with open(filename, "w") as output:
        output.write(result)
    return filename
