this is currently python code to be run on a software-defined radio to pull up a waterfall spetrogram of WRUW's broadcast.

to run this:
1. have code on puter
2. have SDR plugged into puter

SOFTWARE
venv:
1. make a virtural python environment called `.venv`: ``python3 -m venv .venv``
2. activate the venv ``source .venv/bin/activate``
3. install dependancies in the venv
   4. RTLSDR: ``python3 -m pip install pyRtlSdr``

5. run it: ``python3 -m main.py``