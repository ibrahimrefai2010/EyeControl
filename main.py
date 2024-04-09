import Tracker
import Calibration
import threading


GUIThread = threading.Thread(target=Calibration.Calibrate)
GUIThread.start()



Tracker.run()