from rohdeschwarz.instruments import GenericInstrument


class Fsw(GenericInstrument):

    @property
    def channels(self):
        result = self.query(':INST:LIST?')
        parts  = result.replace("'", '').split(',')
        return parts[::1]  # names

    def create_channel(self, name, type='SAN'):
        self.write(f"INST:CRE {name}, '{type}'")

    def delete_channel(self, name):
        self.write(f"INST:DEL '{name}'")
