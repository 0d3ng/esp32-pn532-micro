import NFC_PN532 as nfc
from machine import Pin, SPI

# SPI
spi_dev = SPI(2, baudrate=1000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)
cs.on()
print("Init SPI")

# SENSOR INIT
pn532 = nfc.PN532(spi_dev,cs)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

while True:
    print('Reading...')
    uid = pn532.read_passive_target(timeout=500)
    if uid is None:
        print('CARD NOT FOUND')
    else:
        numbers = [i for i in uid]
        string_ID = '{}-{}-{}-{}'.format(*numbers)
        print('Found card with UID:', [hex(i) for i in uid])
        print('Number_id: {}'.format(string_ID))