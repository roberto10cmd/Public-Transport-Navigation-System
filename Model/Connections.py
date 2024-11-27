
class Connections:
    def __init__(self, from_station_id, to_station_id, distance,connection_id=None):
        self.connection_id=connection_id
        self.from_station_id = from_station_id
        self.to_station_id = to_station_id
        self.distance = distance

