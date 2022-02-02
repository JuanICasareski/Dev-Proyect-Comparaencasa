# **COMPARAENCASA Dev Project**

## **Setup**
1. Install [Python 3.9.9](https://www.python.org/downloads/release/python-399/)
2. Install [Node.js](https://nodejs.org/en/)


**Backend setup:**
1. Open the command prompt
2. Move into the directory with <```cd C:\Users\YourUser\YourDirectory\backend```>
3. Run <```pip install -r requirements.py```>


**Frontend setup:**
1. Open the command prompt
2. Move into the directory with <```cd C:\Users\YourUser\YourDirectory\frontend```>
3. Run <```npm install```>
4. Run <```npm fund```>
   

## **Initialization**


**Backend initialization**
1. Open the command prompt
2. Move into the directory with <```cd C:\Users\YourUser\YourDirectory\backend```>
3. Run <```uvicorn main:app --host <local ip> --port 8000```>

**Frontend initialization**
1. In line 17 of ```frontend/src/components.PlateInput.jsx``` change ```<host ip>``` for the ip of the backend host
2. Open the command prompt
3. Move into the directory with <```cd C:\Users\YourUser\YourDirectory\frontend```>
4. Run <```npm start```>
   

## **Usage**


**Uploading data into de database**
1. Open the command prompt
2. Move into the directory with <```cd C:\Users\YourUser\YourDirectory\backend```>
3. Run <```python3 uploadCarData.py <your json file>```>
   
    Note: the json file must include the extension and respect the following format:
    ![https://imgur.com/a/R0PADpU](https://i.imgur.com/9AAjaRg.png)

**Frontend use**
1. Open ```https://<frontend host ip>:3000```
2. You should get the following structure:
   ![https://imgur.com/a/VKO5p3W](https://i.imgur.com/qjNMyN7.png)
3. Now just type the car plate and expect the car model below the textbox