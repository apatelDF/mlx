from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import csv
import smbus
from time import sleep
import datetime


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
    # Setup the Sheets API
    # Must log into account on browser and aprove use once
    # Must have API key saved as client_secret.json in same directory
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    sensor = MLX90614()
    while(True):
        vals = [[]]
        temp = sensor.get_obj_temp() #get temp
        if(temp > ALERT_TEMP):
            date = str(datetime.datetime.today()).split()[0]
            time = str(datetime.datetime.today()).split()[1]
            # Store vales in a 2d array to be uploaded
            vals[0].append(date)
            vals[0].append(time)
            vals[0].append(str(temp))

            # Call the Sheets API
            body = {
                'values': vals
            }
            result = service.spreadsheets().values().append(
                spreadsheetId = SPREADSHEET_ID,
                range='A1',
                valueInputOption='USER_ENTERED',
                body=body).execute()
