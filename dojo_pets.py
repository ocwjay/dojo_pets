from ninjas import *
from pets import *

jay = Ninja("Jay", "Krow", dog("Piper", "dog", ["sit", "lay down", "roll over"]))
krys = Ninja("Krys", "Prancer", cat("Skittles", "cat", ["scream for food", "hunt", "furiously bat paws at a string"]))
james = Ninja("James", "Farmingtion", hedgehog("Spyke", "hedgehog", ["roll into a ball"]))
gemma = Ninja("Gemma", "Johns", rabbit("Cottonball", "rabbit", ["hop around"]),2)

jay.feed("pet food").feed("treat").walk().bathe()
krys.feed("pet food").feed("treat").walk().bathe()
james.feed("pet food").feed("treat").walk().bathe()
gemma.feed("pet food").feed("treat").feed("treat").feed("treat").walk().bathe()
