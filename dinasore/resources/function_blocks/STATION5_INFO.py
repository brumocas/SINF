import datetime

# This FB implements the STATION1_INFO 

class STATION5_INFO:
    def __init__(self):
        self.status = ""
        self.temperature = ""
        self.humidity = ""
        self.power = ""
        self.luminosity = ""
        self.wood_logs = 0
        self.R = ""
        self.G = ""
        self.B = ""

    def schedule(self, event_input_name, event_input_value, data, state):
        if event_input_name == 'INIT':
            return [event_input_value, None, [], [], [], [], [], [], [], [], [], []]
        
        elif event_input_name == 'RUN':
            # Parse sensor data when available
            if data != '':
                data_list = data.split(',')
                self.temperature = data_list[0]
                self.humidity = data_list[1]
                self.power = data_list[2]
                self.luminosity = data_list[3]
                self.R = data_list[5]
                self.G = data_list[6]
                self.B = data_list[7]
                self.status = data_list[-1]
                self.wood_logs += 1
                return [ None
                        , event_input_value
                        , "OK" if self.status == "0" else "ANOM"
                        , self.temperature
                        , self.humidity
                        , self.power
                        , self.luminosity
                        , str(self.wood_logs)
                        , self.R
                        , self.G
                        , self.B
                        ]
            else :
                return [None
                        , event_input_value
                        , state
                        , state
                        , state
                        , state
                        , state
                        , state
                        , state
                        , state
                        , state
                        ]