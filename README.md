# sc
smartcard stuff

To run python with pyscard without interfering with your python environmemt, use virtualenv:

     virtualenv venv
     cd venv
     . bin/activate
     pip install pyscard
     
Then run for instance

    python yk-getserial.py
