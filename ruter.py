import time, datetime
import requests, json
from time import gmtime,strftime


#dict nedenfor brukes som grunnlag for å legge inn holdeplassvalg i prosjektet
holdeplassValg = {'Rosenhoff':3011405, 'Storo T':3012120,'Grefsen Trikk':3012111,'Sinsen T':3012100}
for holdeplassValg, abbrev in holdeplassValg.items():
	print (holdeplassValg)

#Holdeplass nr 3011405 er Rosenhoff
ruterapi_url = "http://reisapi.ruter.no/StopVisit/GetDepartures/3012120"

#Her henter vi sanntidsdata for holdeplassen
r = requests.get(ruterapi_url)

#Her henter vi ut linjenummer, destinasjon og tid for ankomst
linjenummer = r.json()[0]["MonitoredVehicleJourney"]["LineRef"]
destinasjon = r.json()[0]["MonitoredVehicleJourney"]["DestinationName"]
ankomst = r.json()[0]["MonitoredVehicleJourney"]["MonitoredCall"]["AimedArrivalTime"]

#Her gjoer vi om ankomsttiden fra tekst til et tidsobjekt
t_ankomst = datetime.datetime.strptime(ankomst[:19], "%Y-%m-%dT%H:%M:%S")

#Her henter vi tiden akkurat naa
t_now = datetime.datetime.now()

#Saa gjoer vi om disse tidsobjektene til et standardformat
d1_ts = time.mktime(t_ankomst.timetuple())
d2_ts = time.mktime(t_now.timetuple())

#Naa kan finne ut hvor mange sekunder det er igjen
seconds_left = int(d2_ts-d1_ts)

#Her konverterer vi til minutter
time_left_str = " " + str(seconds_left/60) + " min"

#Vi har totalt 16 tegn paa skjermen. Her regner vi ut hvor mye plass vi har til destinasjonsnavnet
dest_len = 16 - len(time_left_str) - len(linjenummer) - 1

#Fjern tegn det ikke er plass til
destinasjon = destinasjon[:dest_len]

#Vi lager de to linjene med tekst
linje1 = "Rosenhoff: "
linje2 = linjenummer + " " + destinasjon + time_left_str
linjetid = "Klokken er " +strftime("%H:%M")
#Her skriver vi ut resultatet paa PC-skjermen
print ""
print linjetid
print linje1
print linje2
print ""
