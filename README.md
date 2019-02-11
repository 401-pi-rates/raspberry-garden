# raspberry-garden
        Github - https://github.com/401-pi-rates/raspberry-garden

        Authors:
            Ray Ruazol - https://github.com/rpruazol
            Matthew Brown - https://github.com/MthwBrwn
            Joyce Liao - https://github.com/joyliao07


## Description:
    	Monitor the health and overall status of your garden on the go!  Do your plants need to be watered?  Is it too hot?  Too cold?  Too dry?  Too humid?  Find out all these stats all in one place!

## Tech used:
    	Garden:
            RPi (Raspeberry Pi) Model 3
                Rasbian (Debian linux optimized for a Raspberry Pi)
                Python 3.6
                Python GPIO module
                Python Requests module
            Solderless breadboard
                Push button switch x2
                Jumper wires (male to female, male to male)
                LEDs
                1k ohm resister x2
        Website:
            Django framework
            PostgreSQL
            Docker
            Amazon AWS EC2
            Pytest

## Technical general concept:
    	The RPi is connected to the internet and running a script continously until the user exits manually, and looks for a state change coming from the RPi's GPIO pins.  If a change occurs a callback function is called, which sends the information via POST request to the endpoint of our website API.  From there the API unpacks the information and serializes the data, creates a model out of it, and stores the info in the database.  From there the Django app frontend requests the information from the API, and the API retrieves it.

### Stretch goal:
    	The endpoint is set up such that another sensor can be added to the "garden" fairly easily.  Just create a script that reads the GPIO input on the RPi end, create an additional method on the class in the garden_api views then create a model and serializer.  The original idea was to do this for a temperature/humidity sensor, soil moisture (if it needed to be watered or not), fan speed, etc.

#### References
        Raspberry Pi 3 GPIO pinout - https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg
        Elecronics push button switch circuit - https://www.instructables.com/id/Project-3-Push-Button-and-LED/
        Soil moisture sensor - https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/
        Requests module docs - https://www.pythonforbeginners.com/requests/using-requests-in-python
        GPIO module docs - https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
        What is IoT? - https://www.zdnet.com/article/what-is-the-internet-of-things-everything-you-need-to-know-about-the-iot-right-now/
