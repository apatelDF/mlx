from time import sleep
import smbus
import datetime
import paho.mqtt.client as mqtt
import json

ALERT_TEMP = 86 #150

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
    newEmiss = 0

    def __init__(self, address=0x5a, bus_num=1, emiss=1.0):
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)
        self.newEmiss = emiss

    def setEmiss(self, emiss):
        self.newEmiss = emiss

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
        # default emisstivity is 1.0

    def data_to_temp(self, data): # data *.02 = Kelvin
        temp = (data*.036) - 459.67 # Convert to F
        return self.emissAdjustment(temp) #apply new emiss setting

    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)

    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)

    def readDeviceEmiss(self):
        data = self.read_reg(self.MLX90614_EMISS)
        return data/65535.0

    def emissAdjustment(self, tempMeasured):
        return tempMeasured * (1 / self.newEmiss ** 0.25)

    def emissCalibration(self, knownTemperature):
        self.newEmiss = 1.0
        average = 0
        for i in range(10):
            temp = self.get_obj_temp()
            average += (temp/knownTemperature) ** 4

        self.newEmiss = average / 10.0
        print("New Emiss is set to: " + self.newEmiss)

    # def set_emiss(self, emiss): #Not Working
    #     if(emiss < .1 or emiss > 1.0):
    #         return False
    #
    #     toWrite = int(emiss * 65535.0)
    #     print("Attempting to write: " + str(toWrite))
    #     for i in range(self.comm_retries):
    #         try:
    #             self.bus.write_word_data(self.address, self.MLX90614_EMISS, toWrite)
    #         except IOError as e:
    #             sleep(self.comm_sleep_amount)
    
if __name__ == "__main__":
    sensor = MLX90614()

    log = open("log.csv", "a")
    THINGSBOARD_HOST = 'demo.thingsboard.io'
    ACCESS_TOKEN = 'vfNbBlqPnvGcJLcAAnxC'
    sensor_data = {'temperature': 0}
    client = mqtt.Client()

    # Set access token
    client.username_pw_set(ACCESS_TOKEN)
    # Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
    client.connect(THINGSBOARD_HOST, 1883, 60)
    client.loop_start()
    sensor.setEmiss(.98)
    while(True):
        temp = sensor.get_obj_temp() #get temp
        if(temp > ALERT_TEMP):
            print('HIGH HEAT DETECTED')
            timeStamp = str(int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000))
            logString = timeStamp + ", " + str(temp) + "\n"
            log.write(logString)
            # Sending temperature data to ThingsBoard
            sensor_data['temperature'] = temp
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 0)
            sleep(.5)
        print(temp)
    log.close()
    client.loop_stop()
    client.disconnect()
