from rohdeschwarz.instruments import GenericInstrument


print('in module project.fsw')
print('creating class Fsw')
class Fsw(GenericInstrument):

    @property
    def channels(self):
        result = self.query(':INST:LIST?').strip()
        parts  = result.replace("'", '').split(',')
        return parts[1::2]  # names

    def create_channel(self, name, type='SAN'):
        self.write(f"INST:CRE {type}, '{name}'")

    def delete_channel(self, name):
        self.write(f"INST:DEL '{name}'")
