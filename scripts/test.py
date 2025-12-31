import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.joinpath("src")))
print(sys.path)
from ntrip_client.ntrip_client import NTRIPClient

c = NTRIPClient(
    host="120.253.239.161",
    port=8001,
    mountpoint="RTCM33_GRCEJ",
    ntrip_version=None,
    username="cwpm11417",
    password="cfuejdyk",
    logerr=lambda x: print(x),
    logwarn=lambda x: print(x),
    loginfo=lambda x: print(x),
    logdebug=lambda x: print(x)
)
print(c.connect())