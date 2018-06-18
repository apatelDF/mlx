from time import sleep
import datetime
import requests


ALERT_TEMP = 86 #150

#ubidpots API info
TOKEN = 'A1E-I2rDWsU0ogLS6dVD5ZYUsamsyyDWyK'


class MLX90614():

    MLX90614_RAWIR1=0x04
    MLX90614_RAWIR2=0x05
    MLX90614_TA=0x06
    MLX90614_TOBJ1=0x07
    MLX90614_TOBJ2=0x08

    MLX90614_TOMAX=0x20
    MLX90614_TOMIN=0x21
    MLX90614_PWMCTRL=0x22
    MLX90614_TARANGE=0x23
    MLX90614_EMISS=0x24
    MLX90614_CONFIG=0x25
    MLX90614_ADDR=0x0E
    MLX90614_ID1=0x3C
    MLX90614_ID2=0x3D
    MLX90614_ID3=0x3E
    MLX90614_ID4=0x3F

    comm_retries = 5
    comm_sleep_amount = 0.1

    def __init__(self, address=0x5a, bus_num=1):
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)

    def read_reg(self, reg_addr):
        for i in range(self.comm_retries):
            try:
                return self.bus.read_word_data(self.address, reg_addr)
            except IOError as e:
                #"Rate limiting" - sleeping to prevent problems with sensor
                #when requesting data too quickly
                sleep(self.comm_sleep_amount)
        #By this time, we made a couple requests and the sensor didn't respond
        #(judging by the fact we haven't returned from this function yet)
        #So let's just re-raise the last IOError we got
        raise e

    def data_to_temp(self, data): # data *.02 = Kelvin
        temp = (data*.036) - 459.67 # Convert to F
        return temp

    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)

    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)


if __name__ == "__main__":
    sensor = MLX90614()
    print('reading tempature')
    while(True):
        temp = sensor.get_obj_temp() #get temp
        if(temp > ALERT_TEMP):
            print('HIGH HEAT DETECTED')
            date = str(datetime.datetime.today()).split()[0]
            time = str(datetime.datetime.today()).split()[1]

            headers = {'X-API-TOKEN': TOKEN}
            payload = {'Temperature': temp}

            r = requests.post("http://things.ubidots.com/api/v1.6/devices/demo/", data=payload, headers=headers)
            print(r)
