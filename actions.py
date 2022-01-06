from time import sleep


# TODO: add coloured text
def read_story(scene: str, header: str = None, reading_rate: float = 0.08):
    start_reading = False

    if header is not None:
        for char in header:
            print(char, end='')
            sleep(reading_rate * 8) if char == ':' else sleep(reading_rate)
        else:
            print()

    with open('lore.txt', 'r') as file:
        for line in file:
            if line != '\n':
                line = line.strip('\n')

            if start_reading:
                if line == '--end':
                    return
                elif line == '--lineBreak':
                    print()
                else:
                    for char in line:
                        print(char, end='')

                        match char:
                            case ',' | '.':
                                sleep(reading_rate * 8)
                            case _:
                                sleep(reading_rate)

            else:
                if line.split() == ['--scene:', scene]:
                    start_reading = True
        print('No Scene Found')
