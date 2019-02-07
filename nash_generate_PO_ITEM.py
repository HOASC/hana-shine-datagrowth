import string
import random
import csv

sqlschemastring="\"SAP_HANA_DEMO\".\"sap.hana.democontent.epm.data"
sqltablestring="PO.Item\""
sqlstring=sqlschemastring+"::"+sqltablestring

numitems=1000000
base=30010000
last=base+numitems

months=[["Jan",31], ["Feb",28], ["Mar",31], ["Apr",30], ["May",31],["Jun",30],["Jul",31],["Aug",31],["Sep",30],["Oct",31],["Nov",30],["Dec",31]]
history_createdby_employeeid="0000000033"
noteid=""
quantityunit="EA"
products=[["HT-1000","EUR",956.00],["HT-1001","EUR",1249.00],["HT-1002","USD",1570.00],["HT-1003","EUR",1650.00],["HT-1007","USD",499.00],["HT-1010","EUR",1999.00],["HT-1011","JPY",2299.00],["HT-1020","EUR",129.00],["HT-1021","MXN",149.00],["HT-1022","ARS",205.00],["HT-1023","USD",239.00],["HT-1030","EUR",230.00],["HT-1031","GBP",285.00],["HT-1032","EUR",345.00],["HT-1035","USD",399.00],["HT-1036","CAD",430.00],["HT-1037","MXN",1430.00],["HT-1040","EUR",830.00],["HT-1041","ARS",490.00],["HT-1042","EUR",349.00],["HT-1050","RUB",139.00],["HT-1051","USD",99.00],["HT-1052","EUR",170.00],["HT-1055","EUR",99.00],["HT-1056","JPY",119.00],["HT-1060","EUR",9.00],["HT-1061","EUR",7.00],["HT-1062","ARS",11.00],["HT-1063","BRL",14.00],["HT-1064","CAD",16.00],["HT-1065","CHF",26.00],["HT-1066","USD",2.50],["HT-1067","EUR",3.50],["HT-1068","USD",3.50],["HT-1069","JPY",800.00],["HT-1070","ARS",70.90],["HT-1071","ZAR",81.70],["HT-1072","USD",101.20],["HT-1073","EUR",24.00],["HT-1080","INR",51.00],["HT-1081","PLN",89.00],["HT-1082","ARS",169.00],["HT-1083","CNY",520.00],["HT-1085","DKK",1499.00],["HT-1090","EUR",39.00],["HT-1091","EUR",26.00],["HT-1092","EUR",45.00],["HT-1100","USD",89.90],["HT-1101","EUR",79.90],["HT-1102","USD",69.00],["HT-1103","EUR",77.00],["HT-1104","JPY",55.00],["HT-1105","EUR",29.00],["HT-1106","MXN",34.00],["HT-1107","ARS",29.90],["HT-1110","USD",8.90],["HT-1111","EUR",6.90],["HT-1112","GBP",39.00],["HT-1113","EUR",2.30],["HT-1114","USD",69.00],["HT-1115","CAD",42.00],["HT-1116","MXN",36.00],["HT-1117","EUR",38.00],["HT-1118","ARS",79.00],["HT-1120","EUR",260.00],["HT-1137","RUB",1230.00],["HT-1138","USD",1211.00],["HT-1210","EUR",2399.00],["HT-1500","EUR",5000.00],["HT-1501","JPY",15000.00],["HT-1502","EUR",25000.00],["HT-6130","EUR",1459.00],["HT-6131","ARS",1199.00],["HT-6132","BRL",899.00],["HT-7030","CAD",2490.00],["HT-7020","CHF",1490.00],["HT-7010","USD",799.00],["HT-7000","EUR",549.00],["HT-1095","USD",160.00],["HT-1096","JPY",120.00],["HT-1097","ARS",56.00],["HT-6123","ZAR",299.00],["HT-6122","USD",167.00],["HT-6121","EUR",63.00],["HT-6120","INR",45.00],["HT-6111","PLN",288.00],["HT-6110","ARS",130.00],["HT-6102","CNY",889.00],["HT-6101","DKK",679.00],["HT-2002","EUR",853.99],["HT-6100","EUR",469.00],["HT-2027","EUR",24.99],["HT-2026","USD",29.99],["HT-2025","EUR",44.99],["HT-2001","USD",449.99],["HT-2000","EUR",249.99],["HT-1603","JPY",1700.00],["HT-1602","EUR",1200.00],["HT-1601","MXN",900.00],["HT-1600","ARS",600.00],["HT-1119","USD",79.00],["HT-8000","EUR",799.00],["HT-8001","GBP",999.00],["HT-8002","EUR",1199.00],["HT-8003","USD",1388.00],["AD-1000","CAD",0.00]]

ofcsv=open('generated_PO_ITEM.csv','w')
ofsql=open('generated_PO_ITEM.sql','w')
i=base
while i < last:
        purchaseorderid=str(i).zfill(10)
        poitem=random.randint(1,10)
        if(poitem+i) <= last:
                pomax=poitem
                j=1
                while j <= pomax:
                        purchaseorderitem=str(j*10).zfill(10)
                        productnum=random.randint(0,105)
                        product_productid=products[productnum][0]
                        currency=products[productnum][1]
                        grossamnt=products[productnum][2]
                        grossamount=format(products[productnum][2], '.2f')
                        netamount=format((random.uniform(0.85,0.95)*grossamnt), '.2f')
                        taxamount=format((0.16*grossamnt), '.2f')
                        quantity=random.randint(1,3)
                        deliverydate="2014-"+"12"+"-"+str(random.randint(1,months[11][1])).zfill(2)
                        csvstr=purchaseorderid+";"+purchaseorderitem+";"+product_productid+";"+noteid+";"+currency+";"+str(grossamount)+";"+netamount+";"+taxamount+";"+str(quantity)+";"+quantityunit+";"+deliverydate+"\n"
                        sqlstr="insert into "+sqlstring+" VALUES ('" +purchaseorderid+"','"+purchaseorderitem+"','"+product_productid+"','"+noteid+"','"+currency+"','"+str(grossamount)+"','"+netamount+"','"+taxamount+"','"+str(quantity)+"','"+quantityunit+"','"+deliverydate+"');\n"
                        ofcsv.write(csvstr)
                        ofsql.write(sqlstr)
#                        print csvstr
#                        print sqlstr
                        j+=1
                i+=pomax

ofcsv.close()
ofsql.close()
