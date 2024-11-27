
class Stations:

    def __init__(self,name,station_id=None):
        self.station_id=station_id
        self.name=name

    def get_id(self):
        return self.station_id

    def get_name(self):
        return self.name

    def set_id(self,station_id):
        self.station_id=station_id

    def set_name(self,name):
        self.name=name


