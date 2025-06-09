from w0sa.utils.ura_generator import ura_gen

channels = 96
ports = [None for prt in range(1,channels+1)]
attenuations = [None for atn in range(1,channels+1)]

print(ura_gen(channels=channels, ports=ports, attenuations=attenuations))
