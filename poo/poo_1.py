class Jugador:
  def __init__(self, nombre, juego="Tetris", tiene_equipo= False,equipo=None):
    self._nombre = nombre
    self.juego = juego
    self.tiene_equipo = tiene_equipo
    self.equipo = equipo
  def jugar(self):
    if self.tiene_equipo:
      print (f"{self.nombre} juega en el equipo {self.equipo} al{self.juego}")
    else:
      print(f"{self.nombre} juega solo al {self.juego}")
  def __add__(self, otro):
    return (f"Ambos jugadores son {self._nombre} y {otro._nombre}")


nico = Jugador('Nico Villalba', "Guild Esports")
faker = Jugador("Faker", "SK Telecom")
print(nico + faker)