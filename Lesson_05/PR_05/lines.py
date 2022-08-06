def low_reg(line):
    line_low = line.lower()
    return line_low

def up_reg(line):
    line_up = line.upper()
    return line_up
    

lines = 'ОЙ У ЛУЗІ ЧЕРВОНА КАЛИНА ПОХИЛИЛАСЯ'

line_low = list(map(low_reg, lines.split()))
print(' '.join(line_low))

line_up = list(map(up_reg, line_low))
print(' '.join(line_up))
