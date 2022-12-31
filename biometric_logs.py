
from zk import ZK, const
from zk.attendance import Attendance

IP_ADDRESS = "192.168.101.199"
PORT = 4370
TIMEOUT=5

conn = None
zkObj = ZK (
  ip=IP_ADDRESS,
  port=PORT,
  password=1,
  timeout=TIMEOUT,
  ommit_ping=True
)

try:
  print("Connecting...")
  conn = zkObj.connect()

  print("Connected!")
  # conn.disable_device()

  print("Reading attendance records...")
  attendances = conn.get_attendance()

  for attendance in attendances:
    if(attendance.uid == 315):
      print(attendance)

  print("\nLOADED ALL ATTENDANCE!")

  # conn.enable_device()

except Exception as e:
  print("Exception:", e)

