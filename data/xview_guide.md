
# xView

## From UAT Environment

## General Settings

## Contracts

### All contracts have almost the same configuration:

#### Overview GEIParser
This one has a different routing entry compared to the others: `Acc.DO.EInv.GEIParse - InsertInboxOutboxUpdateStatus`.

#### Overview GetDocument / GetToken / SendInv

#### Overview GetInvStatus
In this case, **Message Flow** is different from the others:
- **Buffer Mode**: In Port  
- **Release Schedule**: `Acc.DO.EInv.Trigger.ShortWait`


#### Overview XUE
In this case, **Out Ports** include the `eHubTransaction` contract (this is a special contract in another xView).

#### Contract Settings

#### Message Flow

## Wait Schedule
This component periodically executes the associated contract. If multiple transactions are pending, they will be released simultaneously.

### Overview
The associated contract is `GetInvStatus`.

### Settings

## Application Transport

### ReceiveEndPoint: Acc.DO.App.In

#### Overview

#### Application Transport: xT Settings

### SendEndpoint: Acc.DO.App.Out

#### Overview

#### Application Transport: xT Settings

## Application


### Overview

### Settings

Make sure to generate the GRPC settings file if the connection is not working. Usually, this file is included with the compiled project, but if not, regenerating it may resolve the issue.


Ensure that the file is saved in the correct folder of the handler project, with the same name defined in `appsettings.json`:


In the application folder, open `appsettings.json` to verify how the saved GRPC file should be named.


In this case, the file is named `HostedAppGRPC.json`:

## Application Directory


### Settings

In this case, we add a file named `start.cmd` with a script inside:

Inside the file, write the full URL path of the application:

```
cd C:\xHub\Interfaces\Accounting\XH.Acc.EInvoicing.DominicanRepublic.Interface\XH.Acc.EInvoicing.DominicanRepublic.HostedApplication
XH.Acc.EInvoicing.DominicanRepublic.HostedApplication.exe
```

## Hosted Application


### Overview


## Activation Schedule


### Overview


### Settings

The Activation Schedule can be enabled to execute the `start.cmd` script configured earlier. In this case, it is set to true for testing purposes. It can also be launched manually (and disabled) from the project or by directly running `XH.Acc.EInvoicing.DominicanRepublic.HostedApplication.exe` in the application folder to view console logs (in local environment). If run through the project, it can be debugged.


## Routing Table


### Settings

Add a new Routing Entry with the same name as the contract to be redirected:

In the Routing Entry settings, set the match field as `custom.Acc.Next` and assign the same value defined in the static `Routing` class in the code:


After this, the Routing Table will look like this:

To make all contracts appear in the list, manually select the ones to display:

After this, the program will automatically generate the arrows:
