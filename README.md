# Web-Hook
### File: sender.py
Consists data in dict format that is essential to send to the target.
* Uses JSON modules for making dict data into JSON 
* Simply POSTs the JSON data to the target URL
* "Content-type" header is set to application/json
* You can replace the URL

### File: receiver.py
Works in listen mode for fetching the data.
* Imports flask for creating a website hook to recieve POST data from sender
* Receives data in "dict" type
* Checks for "status" key whether it has "True" or "False"

**Feel free to analyze or customize the script.**  
*No sensitive data has been provided in these scripts.*