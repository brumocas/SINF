import datetime

# This FB implements the STATION1_INFO 

class STATION3_INFO:
    def __init__(self):
        self.status = ""
        self.temperature = ""
        self.humidity = ""
        self.power = ""
        self.luminosity = ""
        self.wood_logs = 0
        self.humidity_washing = ""
        self.Force_drilling = ""
        self.temperature_drying = ""
        self.Gas_varnish = ""
        self.luminosity_curing = ""

    def schedule(self, event_input_name, event_input_value, data, state):
        if event_input_name == 'INIT':
            return [event_input_value, None, [], [], [], [], [], [], [], [], [], [], []]
        
        elif event_input_name == 'RUN':
            # Parse sensor data when available
            if data != '':
                data_list = data.split(',')
                self.temperature = data_list[0]
                self.humidity = data_list[1]
                self.power = data_list[2]
                self.luminosity = data_list[3]
                self.humidity_washing = data_list[5]
                self.Force_drilling = data_list[6]
                self.temperature_drying = data_list[7]
                self.Gas_varnish = data_list[8]
                self.luminosity_curing = data_list[9]
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
                        , self.humidity_washing
                        , self.Force_drilling
                        , self.temperature_drying
                        , self.Gas_varnish
                        , self.luminosity_curing
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
                        , state
                        , state
                        ]