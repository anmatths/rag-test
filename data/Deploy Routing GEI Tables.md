---
Author: Matias Alpuin (MTA)
Reviewed By: Santiago Estevez (S.E)
title: Deploy Routing GEI Tables
source_url: https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/16240/Deploy-Routing-GEI-Tables
tags: [header, xt, xt viewer]
parent: Local Deployment Dominican Republic
children: 
---

#Summary
The purpose of this document is to show you how to deploy the GEI routing table locally. 
Pre-requisites: 
- XT installed locally
- RestAPI service working locally
- Having executed DeployInterfaces.ps1 (to create the base interfaces)

[All this can be done using the xT installation guide](https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/1375/Getting-Started-with-xT). 

##Deploy Routing GEI Tables
- Open proyect **"XH.Acc.EInvoicing.Routing.GEI.Interface"** and **Rebuild -> XH.Acc.EInvoicing.Routing.GEI.Deployment**
![image4.png](/.attachments/image4-5ccd4171-fcd7-4c4c-b110-418dd479e786.png)
Note: If after build the zip folder was not generated, try build in release version

![image.png](/.attachments/image-2f7a7ea7-1c30-4fae-aa78-7a5e0ef4cf77.png)

- This should generate a Zip file in **"C:\git\wtg\eServices\eServices\XH\Products\Accounting\Bin\BAT\"** search the Zip and extract it
![image5.png](/.attachments/image5-36849140-349c-4c4c-90b9-a0626c6daf21.png)

- Open Developer PowerShell for Visual Studio as Admin
![image.png](/.attachments/image-969611fc-8c04-45b9-9d5f-b02ebaf2e718.png)

- Run: `MSBuild "YOUR_EXTRACTED_PATH\Deploy.proj" /t:bat:deploy`
![image.png](/.attachments/image-5ef8e7cf-2bdb-4edd-9983-6e099dbb1638.png)
If you have an error during deploy try reading the message, if error persist ask for help in the team or made a post in integration teams channel. 

- Check result in **xT Administrator**
![image10.png](/.attachments/image10-8b65bcf4-b7fc-4fe9-8827-f48c7613a678.png)
In xt administrator
stream > default > Accounting > !Acc.Routing.GEI > Acc.RoutingTable.GEI (this is of the type routing)

If you added a new entry in the GEI interface project, the new entry must be in Acc.RoutingTable.GEI