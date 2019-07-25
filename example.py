""" Example script to run Mahadiscom library """
from mahadiscomenergybill import MahaDiscomEnergyBill


def main():
    mahadiscomenergybill = MahaDiscomEnergyBill(cn='170020034907', bun='4637', ct='2')
    billdetails = mahadiscomenergybill.get_bill_details()
    print (billdetails)
    print (billdetails['consumerNo'])
    print (billdetails['billMonth'])
    print (billdetails['billAmount'])
    print (billdetails['consumptionUnits'])
    print (billdetails['billDate'])
    print (billdetails['dueDate'])


if __name__ == "__main__":
    main()
