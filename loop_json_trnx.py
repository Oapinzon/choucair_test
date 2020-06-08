from random import choice
from io import open
import numpy

def inicio():
    file = open("postTranx_json.txt","w")
    pt1 = "[\n"
    file.write(pt1)
    

def contenido():   
    listBankId = ["00000001"]
    '''
    listBankId = ["00000001","00000003","00000007","00000018","00000037","00000040","00000042","00000051","00000071","00000076","00000077","00000091","00000106","00000108","00000110","00000115","00000125","00000138","00000139","00000147","00000149","00000150","00000151","00000156","00000157","00000158","00000159","00000160"]
    '''
    numRand = numpy.random.uniform(1,40)
    randDecimal = "{0:.2f}".format(numRand)

    file = open("postTranx_json.txt","a")

    a = """ {
     "customerInfo":{
        "idCustomer":"98829570"
     },
     "beneficiaryInfo":{
        "nameCustomer":"UserOmar_QA",
        "email":"omar.pinzon@banistmo.com"
     },
     "accountDestiny":{
        "accountNumber":"041011142605",
        "accountType":"AHS",
        "bankId":"""
    unity1 = a + '"' + choice(listBankId) + '"' + "\n  "

    b = """},
     "accountOrigin":{
        "accountNumber":"0115932775",
        "accountType":"PRE",
        "bankId":"00000002"\n   """
    #unity2 = b + '"' + choice(listBankId) + '"' + "\n   "

    c = """},
     "transactionCode":"TR",
     "amount":"""
    unity3 = c + '"' + randDecimal + '"'

    d = """,
     "typeMoney":"USD",
     "reference":"prueba1 pOstman",
     "extensions":[
        {
           "idExtension":"email_origin",
           "valueExtension":"omar.pinzon@banistmo.com"
        },
        {
           "idExtension":"phone_number_origin",
           "valueExtension":"66432267"
        }
     ],
     "scheduled": false
     },\n"""
    total = unity1 + b + unity3 + d
    file.write(total)

    file = open("montos_generados.txt","a")
    file.write(randDecimal + "\n")
    file.close
    


def fin():
    file = open("postTranx_json.txt","a")
    pt2 = "]"
    file.write(pt2)
    file.close()

    
inicio()
for i in range(1):
    contenido()
    
fin()