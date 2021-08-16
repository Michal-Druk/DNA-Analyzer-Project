class DnaSequence:
    """
    class that design the DNA sequence data and it's basic methods
    """

    def __init__(self, dna):
        if (all(c in "ACTGactg" for c in dna)):
            self.__dna = dna
        else:
            raise Exception("DNA sequence can contain only A, C, T, G, a, c, t, g")

    def insert(self, dna, index):
        if (type(index) is not int):
            raise Exception("index parameter must be int")
        if (len(self.__dna) <= index):
            raise IndexError
        if (all(c in "ACTGactg" for c in dna)):
            self.__dna = self.__dna[:index] + dna + self.__dna[index:]
        else:
            raise Exception("DNA sequence can contain only A, C, T, G, a, c, t, g")

    def assignment(self, other):
        if (type(other) is str):
            if all(c in "ACTGactg" for c in other):
                self.__dna = other
            else:
                raise Exception("DNA sequence can contain only A, C, T, G, a, c, t, g")
        elif type(other) is type(self):
            self.__dna = other.__dna

    def __str__(self):
        return self.__dna

    def __eq__(self, other):
        return self.__dna == other.dna

    def __ne__(self, other):
        return self.__dna != other.dna

    def __getitem__(self, index):
        return self.__dna[index]

    def __setitem__(self, index, new_val):
        if (type(new_val) is not str):
            raise Exception("DNA sequence must be string")
        if all(c in "ACTGactg" for c in new_val):
            self.__dna = self.__dna[:index] + new_val + self.__dna[index + 1:]
        else:
            raise Exception("DNA sequence can contain only A, C, T, G, a, c, t, g")

    def __len__(self):
        return len(self.__dna)
