import Tracker
import Calibration
import threading


CalibrationThread = threading.Thread(target=Calibration.Calibrate)
CalibrationThread.start()



Tracker.run()