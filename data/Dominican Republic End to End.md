---
Author: Matias Alpuin (MTA)
title: Dominican Republic End to End
source_url: https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/17288/End-to-End
tags: [header, xt, xt viewer]
parent: Dominican Republic eInvoicing
children: 
---

# End to End

## Work item related

- WI00842671 - DO - E-invoicing - End to End for devs
- WI00793899 - DO - E-invoicing - End to End Testing

## [Current UAT - xView](https://devops.wisetechglobal.com/wtg/CargoWise/_wiki/wikis/CargoWise.wiki/17286/UAT-xView)

## Company and Branch
![image.png](/.attachments/image-6651c0d8-0638-4b3b-ae87-b6c958392308.png)

**Form: Company, Branch and Department**

Field, Value
Company, DOI - Dominican Republic eInvoicing Test Company
Branch, SDB - Santo Domingo Branch
Department, BRN - Branch
Button left, Back
Button right, Login

## Main Configuration in CW

### Company RNC

For this this, we need to configure the RNC Emisor to match with the used for Gurusoft (The PAC provider) for test.

```
"Emisor": {
            "RNCEmisor": "131980899", <-
            "RazonSocialEmisor": "GURUSOFT S.R.L.",
            "NombreComercial": "GURUSOFT S.R.L.",
            "DireccionEmisor": "REPUBLICA DOMINICANA",
}
```

For this we need go to Companies and check the organization proxy configured

Maintain > User Admin > Companies
Filter by Country/Region and serch for DO
Then check the column Org. Proxy

If we open the form of any of this organizations we can check the RNC field
RNC: 131980899

### Registry

Maintain > System > Registry
Accounting > E-Reporting and E-Invoicing Configurations > E-Invoicing Testing Suffix for EInvoicingServicePoint (CargoWise Support Only)
In this case we must leave it like this because the default value is “XHUB_DO_EINVOICING” will be used

### Client Registration

#### Client Registration Code

To be able to send the transactions to the PAC we need to configure the corresponding user and password (this is necessary to get the tokens)

Inside a cargowise system we can check the ID in Help > About here we can check a code similar to "WUT-DOI-742"

### Client Registration Page

URL : [Client Registrations](https://ehubportal-test.wtg.zone/ClientRegistrations)
We need to add the client “WUTDOI292” (copied from the Help > About)
for this we need to press the icon "+" in the above section of the form. (is near a pencil icon)

(check Include Non-Prod CW1 System if is a SAND, if the code doesn’t appear then try send a transaction and then check here again)
When the form is open, there will be a few filds to complete. The first one is Client, but here we have to check the "include non prod cw1 system" and press select. In order to list all the codes

After that we have to complete the fields:
Qualifier : DOC
Attribute 1 : usrgurusoft
Password 1 : SENSITIVE$$1$$AES256_HMACSHA256$$ApplicationSecret$$20240828T101010Z$$AAECAwQFBgcICQoLDA0ODw==$$Ett6Fe5dh2gRFCEyVfOLfQ==$$DDFCB3DFE22D2FA65C861167FDA8EC9E6CB7E1F6EB3A850B9296E57EE5835787

Note: The password is generated using a specific encryption method within a code application, which must be requested from a developer. The current code provided by the PAC is encrypted using this method, ensuring that the password remains secure since it only works if the secret key is known.

### How to manage Current Numeration for Transactions

#### Explantion
The PAC assigns a specific number range for each document type. Since these ranges are the only ones available for both SAND environments and the UAT database—and considering that SAND environments are created from a backup of the UAT database which already includes preconfigured compliance sequences—it is essential to manage numbering carefully to avoid conflicts or duplicates.

For this reason, before configuring the compliance sequence books in any environment, an external program must be executed. This program will query the PAC’s API to retrieve the next available number per document type. Based on this information, the corresponding sequences will be configured in CargoWise in alignment with what the PAC assigns.

If, during configuration, the compliance book already set in CargoWise indicates a next available number that differs from what is returned by the PAC’s API, the following corrective process must be applied:
Cancel the number range configured in CargoWise.
Reconfigure the compliance book using the correct number from the API.
This ensures that each document type receives the correct number upon invoicing, preventing rejections from the tax authority due to reused or duplicate numbering.

For more information on how to configure the next number in the compliance sequence, please refer to the document "Dominican Republic Electronic Invoicing Compliance Sequences Testing Configuration…" in WI00793899 - DO - E-invoicing - End to End Testing

### External Program
**Form to complete and search the next available invoice number**
![image.png](/.attachments/image-23de8c1b-db61-436d-a6d3-a7a4f821ad72.png)

### Compliance Sequence
Maintain > Account > Compliance Sequences
![image.png](/.attachments/image-0d23fed5-ed97-474c-843a-ceac0f22914e.png)

# Receivables Transactions

to create a new transaction go to a cargowise sistem and then go to Manage > Receivables > Receivables Transactions : New
![image.png](/.attachments/image-b6ee6df6-6873-451c-9c77-6e5125239f78.png)

## Status DLV
If the response from the DGII is not final, then the status in CW will be 'DLV'.
After a few minutes (configured in the **Wait Schedule** of the **Current UAT - xView**), the application will attempt to retrieve the final status
![image.png](/.attachments/image-2fdc948d-f541-4365-8eea-08d27a525545.png)

## Status FAL
In case there were a error in the invoice the response will be FAL
![image.png](/.attachments/image-1bacbaf1-69cb-4a1e-96f5-e1a91a7a41d5.png)

## Status SUC
If the response from the PAC is successful in CW, the status will change to SUC
![image.png](/.attachments/image-0044f64e-ed08-493d-94c9-ce1ac62ce3fb.png)

## Attached Documents
Inside the transaction in **eDocs** tab there will be two documents. One is the pdf and the other is a XML. Both contains the information of the invoice
![image.png](/.attachments/image-8809cebb-52f6-426c-8753-214da6ee3bbc.png)