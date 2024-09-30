![image](https://github.com/WalkerSchaar/Clipper_Guard/assets/132508530/4484e6f6-0bf1-4105-a027-6eddf9564a56)

Clipper Guard implements logic that restricts the user's clipboard to a single-use state while its running. As soon as a user copies information to the clipboard, they can only paste that information once before Clipper Guard empties the clipboard, resetting it to a clean and safe state. By removing the redundant pasting functionality, Clipper Guard can then monitor for breaks in the logic chain which can identify the detonation of a clipper's stealthy payload. Once it has detected that a populated clipboard's information has changed to a different string of information, the clipboard is immediately emptied to prevent the corrupted transaction from taking place and the user is given a pop-up alert to notify that tomfoolery is afoot.

***DESIGNED FOR WINDOWS COMPUTERS - ANY OTHER SYSTEM WONT RUN***

**INSTALLATION**
git clone https://github.com/WalkerSchaar/Clipper_Guard.git

cd Clipper_Guard

pip install -r requirements.txt

python Clipper_Guard.py

**CONVERT TO AN EXECUTABLE**
pip install pyinstaller

cd path\to\your\Glipper_Guard

pyinstaller --onefile Clipper_Guard.py

*It's highly recommended to rename your exe to a custome file name. This can help prevent clippers from finding and killing a running instance.* 






