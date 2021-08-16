class DnaSequenceData:
    """
    class that design the program data and it's basic methods, using Singleton design pattern
    """
    __instance = None
    __sequence = {}
    __dna_data_by_id = {}
    __dna_data_by_name = {}
    __next_id = 1
    __batch = {}

    def __new__(cls, *args, **kwargs):
        if not DnaSequenceData.__instance:
            DnaSequenceData.__instance = object.__new__(cls)
        return DnaSequenceData.__instance

    def get_dna_data_by_id(self):
        return DnaSequenceData.__dna_data_by_id

    def get_dna_data_by_name(self):
        return DnaSequenceData.__dna_data_by_name

    def get_dna_id(self, name):
        if name not in DnaSequenceData.__dna_data_by_name: raise Exception("The name does not exist in the system")
        return DnaSequenceData.__dna_data_by_name[name]['id']

    def get_dna_name(self, id):
        if id not in DnaSequenceData.__dna_data_by_id: raise Exception("The ID does not exist in the system")
        return DnaSequenceData.__dna_data_by_id[id]['name']

    def get_next_id(self):
        return DnaSequenceData.__next_id

    def set_next_new_seq_name(self, name):
        DnaSequenceData.__next_new_seq_name = name

    def set_next_id(self, id):
        DnaSequenceData.__next_id = id

    def get_sequence_by_id(self, id):
        return DnaSequenceData.__sequence[id]["seq"]

    def set_seq_status(self, id, status):
        DnaSequenceData.__sequence[str(id)]["status"] = status

    def get_seq_status(self, id):
        return DnaSequenceData.__sequence[str(id)]["status"]

    def add_sequence(self, name, new_dna_sequence, status, id=None):
        if id == None:
            old_id = id
            id = DnaSequenceData.__next_id
        else:
            old_id = id
        DnaSequenceData.__sequence[str(id)] = {
            "seq": new_dna_sequence,
            "status": status
        }

        DnaSequenceData.__dna_data_by_id[str(id)] = {
            'name': name,
            'sequence': id
        }
        DnaSequenceData.__dna_data_by_name[name] = {
            'id': id,
            'sequence': id
        }
        if old_id == None:
            DnaSequenceData.__next_id += 1

    def delete_sequence(self, id, name):
        del DnaSequenceData.__sequence[str(id)]
        del DnaSequenceData.__dna_data_by_id[str(id)]
        del DnaSequenceData.__dna_data_by_name[name]

    def add_batch(self, name, batch):
        DnaSequenceData.__batch[name] = batch

    def get_batch_names(self):
        return DnaSequenceData.__batch.keys()

    def get_batch(self, name):
        return DnaSequenceData.__batch[name]
