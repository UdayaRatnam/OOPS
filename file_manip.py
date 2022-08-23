



if __name__ == "__main__":

    print("hello")
    with open('vehicles.txt') as f:
        for line in f:
            line = line.strip()
            if len(line) != 0:
                print(line)
