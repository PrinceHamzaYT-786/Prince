import random
import os
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH:RED
H = '\x1b[1;92m' # HIJAU:GREEN
K = '\x1b[1;93m' # KUNING:YELLOW
B = '\x1b[1;94m' # BIRU:BLUE
U = '\x1b[1;95m' # UNGU:PINK
O = '\x1b[1;96m' # BIRU MUDA: Light Green
N = '\x1b[0m'    # WARNA MATI: Normal Colour
A = '\x1b[1;90m' # WARNA ABU ABU:Light Black
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
random_colours = random.choice([P,M,H,K,B,U,O,N,A,BN,BBL,BP,BB,BK,BH,BM,BA])
print(f'{random_colours} COMMAND OFF DURING BOARD EXAMS ')
