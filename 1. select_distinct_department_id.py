import pandas as pd
data={
    'DEPARTMENT_ID':[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270],
    'DEPARTMENT_NAME':['Administration','Marketing','Purchasing','Human Resources','Shipping','IT','Public Relations','Sales','Executive','Finance',' Accounting','Treasury','Corporate Tax','Control And Credit','Shareholder Services','Benefits','Manufacturing','Construction','Contracting','Operations','IT Support','NOC',' IT Helpdesk','Government Sales','Retail Sales','Recruiting','Payroll'],
    'MANAGER_ID':[200,201,114,203,121,103,204,145,100,108,205,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    'LOCATION_ID':[1700,1800,1700,2400,1500,1400,2700,2500,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700,1700]
    }
employees=pd.DataFrame(data)
dist_id=employees['DEPARTMENT_ID'].unique()
dist_df=pd.DataFrame({'DEPARTMENT_ID': dist_id})
print(dist_df)
