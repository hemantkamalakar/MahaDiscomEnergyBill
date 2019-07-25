import requests
import json
import time

class MahaDiscomEnergyBill(object):
    """ Class to get energy bill from Mahadiscom website """
    def __init__(self, cn, bun, ct):
        """ __init__ """
        self.serverurl = 'https://wss.mahadiscom.in/wss/'
        self.con_details = {}
        self.con_details['ConsumerNo'] = cn
        self.con_details['BuNumber'] = bun
        self.con_details['consumerType'] = ct

    def get_bill_details(self):
        billdetails = {}
        actionurl = "wss?uiActionName=postViewPayBill&IsAjax=true"
        url = self.serverurl + actionurl
        print(url, self.con_details)
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        try:
            response = requests.post(url, headers=headers, data=self.con_details, timeout=10)
            print(response.text)
            billdetails = json.loads(response.text)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")

        if response.status_code == 200:
            return billdetails
        else:
            print("ERROR: Return code is : %d" % response.status_code)
            return {}


def main():
    mahadiscom = MahaDiscomEnergyBill(cn='170850116400', bun='4860', ct='2')
    billdetails = mahadiscom.get_bill_details()
    print ("consumerNo", billdetails['consumerNo'])
    print ("billMonth",  billdetails['billMonth'])
    print ("billAmount", billdetails['billAmount'])
    print ("consumptionUnits", billdetails['consumptionUnits'])
    print ("billDate", billdetails['billDate'])
    print ("dueDate", billdetails['dueDate'])
    print ("promptPaymentDate", billdetails['promptPaymentDate'])
    val = billdetails['promptPaymentDate'].split('(', 1)[1].split(')')[0]
    print(time.strftime("%d-%b-%Y", time.localtime(int(val)/1000)))

if __name__ == "__main__":
    main()
