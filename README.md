# Hello Garage

## Team Rollin' In
- Harsh Baid
- Purnadip Manna
- Ishika Ghosh
- Pratik Agarwal

____
## INDEX
____

1. Installation Process
2. Deployed Prototype
3. Working Endpoints
4. Car No Detection System
5. Workflow
6. Yet to Implement
____

## 1. Installation Process
1. Install Django

`pip install django`

2. Install Twilio

`pip install twilio`

3. Run the Server

`python manage.py runserver`

## 2. Deployed Prototype
We have deployed our project on Heroku and here is the link:
https://hello-garage-hg.herokuapp.com/

> Credential:
>
> Email: admin@gmail.com
>
> Password: password

## 3. Working Endpoints

**For Admin:**

- Landing Page (http://hello-garage-hg.herokuapp.com/)
- Admin Dashboard (http://hello-garage-hg.herokuapp.com/dashboard/)
> _*Garage's Admin have to log in first to go to Dashboard_
- Login (https://hello-garage-hg.herokuapp.com/user/login/)
- Admin Panel (http://hello-garage-hg.herokuapp.com/gapp/)
> Get all the informations of Vehicles which are currenty inside the Parking

**For End User:**

- Register Phone No with Car no (http://hello-garage-hg.herokuapp.com/gapp/update/\<carno>/\<garageid>)
> Open a page to enter Phone Number for OTP verification and registration of Phone Number on successfully verification.

- Verify OTP (http://hello-garage-hg.herokuapp.com/gapp/votp)
> Open a page to enter OTP and verification

**For Backend Operation Purpose:**
- New Entry of Vehicle (http://hello-garage-hg.herokuapp.com/gapp/newvehicle) [data ={ GarageID, NewCarNo }]
> This endpoint will be triggered by CarNoDetection System when a new car number will be detected at the front of the gate.

- Exit & Amount Calculation of a registerd Vehicle (http://hello-garage-hg.herokuapp.com/gapp/exitverify/\<carno>/\<garageid>)
> Fetch Details of registerd vehicle and send OTP to the registered Phone Number and redirect to OTP verification Page.

## 4. Car Number Detection System
- It is a separate system from our main Backend. It will be installed in every garage.
- Take snap of Car's front face at Entry Time.
- Detect Car Number.
- Send the Car Number to our main Backend to instantiate a record for new vehicle.
- Generate a QR (*Register Phone No with Car no*)
- After successful register, Gate of entry point will be opened.
- At the time of exit, Take snap of Car's front face.
- Generate a QR (*Exit & Amount Calculation of a registerd Vehicle*)
- After successful payment, Gate of exit point will be opened.

## 5. Workflow


## 6. Yet to Implement