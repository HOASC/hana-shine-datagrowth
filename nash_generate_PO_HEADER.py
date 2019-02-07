import string
import random
import csv

sqlschemastring="\"SAP_HANA_DEMO\".\"sap.hana.democontent.epm.data"
sqltablestring="PO.Header\""
sqlstring=sqlschemastring+"::"+sqltablestring

numitems=1000000
base=30010000
last=base+numitems

months=[["Jan",31], ["Feb",28], ["Mar",31], ["Apr",30], ["May",31],["Jun",30],["Jul",31],["Aug",31],["Sep",30],["Oct",31],["Nov",30],["Dec",31]]
history_createdby_employeeid="0000000033"
noteid=""
currency="EUR"
combinations=[["N","I","I","I","I"],["C","A","S","I","D"],["P","I","C","I","I"],["X","R","X","I","I"],["P","I","S","I","I"],["R","R","X","I","I"],["P","A","S","I","I"],["P","A","C","I","I"]]

ofcsv=open('generated_PO_HEADER.csv','w')
ofsql=open('generated_PO_HEADER.sql','w')
for i in range(base,last):
        purchaseorderid=str(i).zfill(10)
        rmonth=random.randint(0,11)
        history_createdat= "2014-"+str(rmonth+1).zfill(2)+"-"+str(random.randint(1,months[rmonth][1])).zfill(2)
        history_changedby_employeeid=history_createdby_employeeid
        history_changedat=history_createdat
        partner_partnerid=str(random.randint(0,44)+100000000).zfill(10)
        grossamnt=random.uniform(1.00,9999999.99)
        netamount=(format((grossamnt * 0.90), '.2f'))
        taxamount=format((grossamnt * 0.05), '.2f')
        grossamount=format(grossamnt, '.2f')
        combo=random.randint(0,7)
        lifecyclestatus=combinations[combo][0]
        approvalstatus=combinations[combo][1]
        confirmstatus=combinations[combo][2]
        orderingstatus=combinations[combo][3]
        invoicingstatus=combinations[combo][4]
        csvstr=purchaseorderid+";"+history_createdby_employeeid+";"+history_createdat+";"+history_changedby_employeeid+";"+history_changedat+";"+noteid+";"+partner_partnerid+";"+currency+";"+str(grossamount)+";"+netamount+";"+taxamount+";"+lifecyclestatus+";"+approvalstatus+";"+confirmstatus+";"+orderingstatus+";"+invoicingstatus+"\n"
        sqlstr="insert into "+sqlstring+" VALUES ('" +purchaseorderid+"','"+history_createdby_employeeid+"','"+history_createdat+"','"+history_changedby_employeeid+"','"+history_changedat+"','"+noteid+"','"+partner_partnerid+"','"+currency+"','"+str(grossamount)+"','"+netamount+"','"+taxamount+"','"+lifecyclestatus+"','"+approvalstatus+"','"+confirmstatus+"','"+orderingstatus+"','"+invoicingstatus+"');\n"

        ofcsv.write(csvstr)
        ofsql.write(sqlstr)
#        print csvstr
#        print sqlstr
ofcsv.close()
ofsql.close()
