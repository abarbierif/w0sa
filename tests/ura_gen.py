def ura_gen(
        channels: int = 96,
        spacing: int = 1,
        power: float = 2.7
) -> str:

    """Generates a basic ura command (asumes that channel 1 has the high power)"""

    # check boundaries
    MAX_CHANNELS = 386
    MIN_CHANNELS = 1

    if channels < MIN_CHANNELS or channels > MAX_CHANNELS:
        print(f"Error: the number of channels must be between ({MIN_CHANNELS},{MAX_CHANNELS})")
        return

    ports = []
    while len(ports) < channels:
        ports.append(1)
        for sp in range(spacing):
            ports.append(2)

    ura_command = 'ura '
    attenuation = 0.0
    for ch,prt in zip(range(1,channels+1),ports):
        if ch != channels:
            ura_command += str(ch) + ',' + str(prt) + ',' + str(attenuation) + ';'
        else:
            ura_command += str(ch) + ',' + str(prt) + ',' + str(attenuation)

    return ura_command

if '__main__' == __name__:
    print(ura_gen())
