def ura_gen(
        channels: int = 386,
        ports: list = None,
        attenuations: list = None,

) -> str:

    """Generates an URA command"""

    if ports is None:
        ports = [None for prt in range(1,channels+1)]

    if attenuations is None:
        attenuations = [None for atn in range(1,channels+1)]

    # check boundaries
    MAX_CHANNELS = 386
    MIN_CHANNELS = 1

    if channels < MIN_CHANNELS or channels > MAX_CHANNELS:
        print(f"Error: the number of channels must be between ({MIN_CHANNELS},{MAX_CHANNELS})")
        return

    ura_command = 'URA '
    for ch,prt,atn in zip(range(1,channels+1),ports,attenuations):
        ura_command += str(ch) + ',' + str(prt) + ',' + str(atn) + ';'

    return ura_command[:-1]

if '__main__' == __name__:
    print(ura_gen())

