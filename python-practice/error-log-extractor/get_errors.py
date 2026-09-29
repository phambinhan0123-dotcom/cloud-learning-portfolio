def get_errors(filename: str) -> list:
    errors = []
    with open(filename, "r") as f:
        
        
        for line in f:
            if line.startswith("ERROR:"):
                errors.append(line[7:].strip("\n"))

    return errors
        





if __name__ == "__main__":
    errors = get_errors("server.log")
    print(errors)
