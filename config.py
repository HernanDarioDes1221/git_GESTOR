import sys

DATABASE_PATH = "clientes.csv"

# En la primera posicion siempre se guarda el nombre del scrip

if "pytest" in sys.argv[0]:
    DATABASE_PATH  = "tests/clientes_test.csv"


