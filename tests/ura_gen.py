def ura_gen(
        channels: int = 96,
        spacing: int = 1,
        power: float = 2.7
) -> str:

    """Generates a basic ura command (asumes that channel 1 has high power)"""

    # check boundaries
    MAX_CHANNELS = 386
    MIN_CHANNELS = 1

    if channels < MIN_CHANNELS or channels > MAX_CHANNELS:
        print(f"Error: the number of channels must be between ({MIN_CHANNELS},{MAX_CHANNELS})")
        return

    ports = []
    while len(ports) < channels:
        ports.append(2)
        for sp in range(spacing):
            ports.append(5)

    ura_command = 'URA '
    attenuation = []
    attenuate = False
    for _ in range(channels):
        if attenuate:
            attenuation.append(20.0)
            attenuate = False
        else:
            attenuation.append(0.0)
            attenuate = True

    for ch,prt,atn in zip(range(1,channels+1),ports,attenuation):
        ura_command += str(ch) + ',' + str(prt) + ',' + str(atn) + ';'

    return ura_command[:-1]

if '__main__' == __name__:
    print(ura_gen(channels=48))
