def dcc_gen(
        channels: int = 386,
        slots: int = 1,
        centered: bool = False
) -> str:

    """Generates a dcc command"""
    
    # check boundaries
    MAX_CHANNELS = 386
    MIN_CHANNELS = 1
    MAX_SLOTS = 386
    MIN_SLOTS = 1

    if channels < MIN_CHANNELS or channels > MAX_CHANNELS:
        print(f"Error: the number of channels must be between [{MIN_CHANNELS},{MAX_CHANNELS}]")
        return
    if slots < MIN_SLOTS or slots > MAX_SLOTS:
        print(f"Error: the number of slots must be between [{MIN_SLOTS},{MAX_SLOTS}]")
        return
    if channels * slots > MAX_SLOTS:
        print(f"Error: Exceeded slots! reduce the number of slots per channel or the number of channels")
        return


    dcc_command = 'DCC '
    for ch,sl in zip(range(1,channels+1),range(1,MAX_SLOTS+1,slots)):
        dcc_command += str(ch) + '=' + str(sl) + ':' + str(sl+(slots-1)) + ';'

    return dcc_command[:-1]


if '__main__' == __name__:
    print(dcc_gen(channels=96,slots=4))

