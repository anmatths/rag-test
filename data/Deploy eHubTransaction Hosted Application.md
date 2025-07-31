---
Author: Matias Alpuin (MTA)
Reviewed By: Santiago Estevez (S.E)
title: Deploy eHubTransaction Hosted Application
source_url: https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/16243/Deploy-eHubTransaction-Hosted-Application
tags: [header, xt, xt viewer]
parent: Local Deployment Dominican Republic
children: 
---

##Deploy eHubTransaction Hosted Application

- Open proyect **"XH.Products.EServices.EHubTransactions"** and **Modify:**

  **_Note: All this changes has not to be commited to the repo_**

  - **..\Deployment\Profiles\Local\Configuration.json**

    Copy the content of **"..\Deployment\Profiles\Test401\Configuration.json"** in **"..\Deployment\Profiles\Local\Configuration.json"**

    ![image.png](/.attachments/image-75059af8-2c02-475e-9040-2804665f7c50.png)

    Go to xt administartor > Server Resource > [your current] server configuration (eg JS4HCD54) > right clic > Copy > Id
    Modify **"hostedapp.serverarea"** in **"..\Deployment\Profiles\Local\Configuration.json"** and paste the the Server Configuration id inside the "ValueVector" : ["{\"id\":\"here goes the id\","\str\":1}"]

    ![image.png](/.attachments/image-443183ad-9b9b-40bf-90d0-e74011dce525.png)

  - inside **..\Deployment\Profiles\Local\Deployment.json**

    Modify **UserToken** and **ConnectionString**

    For UserToken you have to create a token in xT adminsitrator and paste the value there (be sure of copy and save this, because after is not possible, and you will need to create a new one)
    For ConnectionString you have to copy the value from other Deployment.json (in this case from the Profile\Test401\)

    ![image.png](/.attachments/image-00a1c146-6fc5-4ad1-b229-fa5836d6fa16.png)

  - **ConnectionString:** need to be copyed from **"..\Deployment\Profiles\Test401\Deployment.json"**

    ![image.png](/.attachments/image-23d111c8-fa27-4648-a201-9a9c25c0261b.png)

  - **UserToken:** Need to be configurated in the **"xT Administrator"**

    ***(xhubdev has to be only in the admins groups)***
    The token has to be created inside the xhubdev user, this user has to be in the group of admins (and only there)
    ![image.png](/.attachments/image-cf2bc37c-92e2-443e-b22b-c9b1e5171f07.png)
    ![image.png](/.attachments/image-d7d8d4d9-8ead-41a6-8286-8421df487dff.png)
    ![image.png](/.attachments/image-3f99c17e-2e14-4cf9-966a-74c013a573fa.png)

- **Rebuild -> XH.Products.EServices.EHubTransactions.HostedApplication.Deployment**

  ![image.png](/.attachments/image-b1b52234-26ce-40fd-9b44-4c381c674a20.png)

- This should generate a Zip file in **"C:\git\wtg\eServices\eServices\XH\Products\EServices\Bin\BAT\"** search the Zip and extract in **"C:\Temp\EHubTransactions\\"**

  ![image39.png](/.attachments/image39-7b7d3724-679c-4e67-a644-821bf1607cf5.png)

- Open Developer PowerShell for Visual Studio as **Administrator**

  ![image.png](/.attachments/image-969611fc-8c04-45b9-9d5f-b02ebaf2e718.png)

- Run: `dotnet msbuild "C:\Temp\EHubTransactions\Deploy.proj" /t:bat:deploy /p:Profile=Local /p:BinPath="C:\git\wtg\eServices\eServices\XH\Products\EServices\EHubTransactions\EHubTransactions\bin" /p:DAT_IS_BUILDING=false` _(/p:DAT_IS_BUILDING=false could be or not neccessary)_
_old run: `MSBuild "C:\Temp\EHubTransactions\Deploy.proj" /p:Profile="Local" /t:bat:deploy` (not working at the moment)_

  ![image.png](/.attachments/image-000e3723-ad43-425a-ae11-7efa1113271d.png)

- Result in **xT Administrator**
After doing all this, if you refresh the view, you will see the diagram and the ehubtransaction should be running in the task manager
  ![image45.png](/.attachments/image45-a7e2490c-9b43-45e8-b47f-5dc8786db67c.png)