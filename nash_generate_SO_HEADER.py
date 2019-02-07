import string
import random
import csv

sqlschemastring="\"SAP_HANA_DEMO\".\"sap.hana.democontent.epm.data"
sqltablestring="SO.Header\""
sqlstring=sqlschemastring+"::"+sqltablestring

numitems=1000000
base=500001029
last=base+numitems

months=[["Jan",31], ["Feb",28], ["Mar",31], ["Apr",30], ["May",31],["Jun",30],["Jul",31],["Aug",31],["Sep",30],["Oct",31],["Nov",30],["Dec",31]]
noteid=""
currency="EUR"
combinations=[["X","I","I"],["N","I","I"],["P","I","D"],["C","P","D"],["P","P","I"],["P","I","I"],["P","P","D"]]

ofcsv=open('generated_SO_HEADER.csv','w')
ofsql=open('generated_SO_HEADER.sql','w')

for i in range(base,last):
    salesorderid=str(i).zfill(10)
    employeeid=random.randint(1,33)
    history_createdby_employeeid=str(employeeid)
    rmonth=random.randint(0,11)
    rday=random.randint(1,months[rmonth][1])
    rmod=random.randint(1,10)
    ryear=random.randint(2013,2015)
    history_createdat= str(ryear)+"-"+str(rmonth+1).zfill(2)+"-"+str(rday).zfill(2)
    history_changedby_employeeid=history_createdby_employeeid
    if (rday+rmod) < months[rmonth][1]:
        history_changedat= str(ryear)+"-"+str(rmonth+1).zfill(2)+"-"+str(rday+rmod).zfill(2)
    else:
        rday=1
	rmonth=rmonth+1
        if (rmonth) > 11:
            ryear=ryear+1
            rmonth=0
        history_changedat= str(ryear)+"-"+str(rmonth+1).zfill(2)+"-"+str(rday+rmod).zfill(2)
    partner_partnerid=str(random.randint(1,33))
    grossamnt=random.uniform(1.00,999999.99)
    grossamount=format(grossamnt, '.2f')
    netamount=format((0.85*grossamnt), '.2f')
    taxamount=format((0.16*grossamnt), '.2f')
    combo=random.randint(0,6)
    lifecyclestatus=combinations[combo][0]
    billingstatus=combinations[combo][1]
    deliverystatus=combinations[combo][2]
    csvstr=salesorderid+";"+history_createdby_employeeid+";"+history_createdat+";"+history_changedby_employeeid+";"+history_changedat+";"+noteid+";"+partner_partnerid+";"+currency+";"+str(grossamount)+";"+netamount+";"+taxamount+";"+lifecyclestatus+";"+billingstatus+";"+deliverystatus+";"+"\n"
    sqlstr="insert into "+sqlstring+" VALUES ('" +salesorderid+"','"+history_createdby_employeeid+"','"+history_createdat+"','"+history_changedby_employeeid+"','"+history_changedat+"','"+noteid+"','"+partner_partnerid+"','"+currency+"','"+str(grossamount)+"','"+netamount+"','"+taxamount+"','"+lifecyclestatus+"','"+billingstatus+"','"+deliverystatus+"');\n"

    ofcsv.write(csvstr)
    ofsql.write(sqlstr)
#    print csvstr
#    print sqlstr


ofcsv.close()
ofsql.close()
