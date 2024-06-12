class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con el valor dado y sin un siguiente nodo
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        # Representación de cadena del nodo para fines de depuración
        return f"Nodo({self.valor})"

class ListaEnlazada:
    def __init__(self):
        # Inicializa la lista enlazada sin ningún nodo (cabeza vacía)
        self.cabeza = None

    def agregar(self, valor):
        # Crea un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si la lista no está vacía, recorre hasta el final y agrega el nuevo nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        # Busca el nodo con el valor dado y lo elimina de la lista
        actual = self.cabeza
        anterior = None
        while actual and actual.valor != valor:
            # Recorre la lista buscando el nodo
            anterior = actual
            actual = actual.siguiente
        if not actual:
            # Si no se encuentra el nodo, retorna False
            return False
        if not anterior:
            # Si el nodo a eliminar es la cabeza, actualiza la cabeza
            self.cabeza = actual.siguiente
        else:
            # Si el nodo está en medio o al final, actualiza las referencias
            anterior.siguiente = actual.siguiente
        return True

    def mostrar(self):
        # Retorna una lista con los valores de todos los nodos
        actual = self.cabeza
        elementos = []
        while actual:
            # Recorre la lista y agrega los valores a la lista 'elementos'
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

class GestionPlaylist:
    def __init__(self):
        # Inicializa la gestión de la playlist con una lista enlazada vacía
        self.playlist = ListaEnlazada()

    def agregar_cancion(self, cancion):
        # Agrega una canción a la playlist
        self.playlist.agregar(cancion)
        print(f'Canción "{cancion}" añadida a la playlist.')

    def eliminar_cancion(self, cancion):
        # Elimina una canción de la playlist
        if self.playlist.eliminar(cancion):
            print(f'Canción "{cancion}" eliminada de la playlist.')
        else:
            print(f'Canción "{cancion}" no encontrada en la playlist.')

    def mostrar_playlist(self):
        # Muestra todas las canciones de la playlist
        canciones = self.playlist.mostrar()
        if canciones:
            print("Playlist:")
            for cancion in canciones:
                print(f'- {cancion}')
        else:
            print("La playlist está vacía.")

# Ejemplo de uso
if __name__ == "__main__":
    gestion_playlist = GestionPlaylist()
    gestion_playlist.agregar_cancion("Song 1")
    gestion_playlist.agregar_cancion("Song 2")
    gestion_playlist.mostrar_playlist()
    gestion_playlist.eliminar_cancion("Song 1")
    gestion_playlist.mostrar_playlist()
