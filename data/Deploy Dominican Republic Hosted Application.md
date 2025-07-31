---
Author: Matias Alpuin (MTA)
Reviewed By: Santiago Estevez (S.E)
title: Deploy Dominican Republic Hosted Application
source_url: https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/16242/Deploy-Dominican-Republic-Hosted-Application
tags: [header, xt, xt viewer]
parent: Local Deployment Dominican Republic
children: 
---

#Deploy Dominican Republic Hosted Application

##1 - Update ServerConfiguration

Open proyect **"XH.Acc.EInvoicing.DominicanRepublic"** and **Modify -> ..\Deployment\Deployment.json**

![image.png](/.attachments/image-1085402c-e84c-474f-98fa-a415019144c8.png)

Set your own local **"xt Administrator"** Server Configuration id in this field: **"ServerConfiguration"**

**_Note: This changes has not to be commited to the repo_**

![image.png](/.attachments/image-6b739a6b-2664-46de-b682-5533e7eba35c.png)
Go to xt administartor > Server Resource > [your current] server configuration (eg JS4HCD54) > right clic > Copy > Id
Paste the Id in the Deployment.json inside the proyect XH.Acc.EInvoicing.DominicanRepublic > XH.Acc.EInvoicing.DominincanRepublic.Deployment > Deployment > Deployment.json
Inside the json Deployment.json go to section "Configuration.json" : { "variables" : { "serverConfiguration" : "Paste Here the Id copyed before" } }

##2 - Generate ZIP file

**Rebuild -> XH.Acc.EInvoicing.DominicanRepublic.Deployment**

![image.png](/.attachments/image-7b9050b3-8d49-443b-8009-90ab642ea74d.png)

For generate this file, probably is neccessary change the proyect from debug to release before rebuilding
This should generate a Zip file in **"C:\git\wtg\eServices\eServices\XH\Products\Accounting\Bin\BAT\"** search the Zip and extract it

![image12.png](/.attachments/image12-23ba7767-b1fd-4792-9867-37a4c68edbc0.png)

##3 - Deploy solution

Open Developer PowerShell for Visual Studio as **Administrator**

![image.png](/.attachments/image-969611fc-8c04-45b9-9d5f-b02ebaf2e718.png)

Run: `MSBuild "YOR_EXTRACT_PATH\Deploy.proj" /t:bat:deploy`

![image.png](/.attachments/image-cd9b98a5-2729-47cd-b1e0-f11789f70d30.png)

Result in **xT Administrator**

![image.png](/.attachments/image-90776fb8-8eb0-442b-a6bd-1c080a1d6035.png)

If you configured your hosted application and deploy options correctly, the hosted application must be started automatically.

To check the new diagram go to XT Administrator and refresh the view.

##4 - Posible errors
1. In case of error try restart the services in xT System Manager (look for this pressing the buton of windows and writing "XT")
1. In case of that doesnt work, some time is neccessary restar the machine.