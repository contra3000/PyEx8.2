import pickle

class Vehiculo:
    nombre = ""
    cc = 0

    def __init__(self, nombre, cc):
        self.nombre = nombre
        self.cc = cc

    def getData(self):
        return self.nombre, self.cc


def main():
    v01 = Vehiculo("Amarok", 2.0)

    print(v01.getData())

    f = open('data.bin', 'wb')
    pickle.dump(v01, f)             # Guardando datos
    f.close()

    f = open('data.bin', 'rb')
    vloaded01 = pickle.load(f)      # Recuperando datos
    f.close()

    print(vloaded01.getData())


if __name__ == '__main__':
    main()
