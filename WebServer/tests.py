#db.execute_command("SELECT * FROM BASE")
from metrodb import MetroDB
db = MetroDB('guest', 'guest')
db.connect()
print("Connected!")


#INSERT INTO BUS_ROUTE Values ("Federal Way TC", "Tukwila International Blvd Link Station", "671", 127);
A = '372'
print("Where does route " + str(A)  + " stop?")
stops = db.execute_command("SELECT BS.Stop_Name FROM BUS_ROUTE AS BR, BUS_STOP AS BS, BUS_ROUTE_STOPS AS BRS WHERE BRS.Stop_ID = BS.Stop_ID AND BRS.Route_number = BR.Route_number AND BR.Route_number = \'" + str(A) +"\' GROUP BY BS.Stop_Name;")

arr = []
for stop in stops:
    arr.append(stop[0])

print(arr)

A = 'University District'
B = 'Wallingford'
print("How do I get from " + A + "to " + B)
baseTable = db.execute_command("SELECT BR.Route_number FROM BUS_ROUTE_STOPS BRS INNER JOIN BUS_ROUTE BR ON BRS.Route_number = BR.Route_number INNER JOIN BUS_STOP BS ON BS.Stop_ID = BRS.Stop_ID WHERE BS.Stop_Name = \'" + A +  "\' OR BS.Stop_Name = \'" + B + "\' GROUP BY BR.Route_number;")

print(baseTable)

A = '372'
print("When will my bus arrive?")
baseTable = db.execute_command("SELECT BRS.ETA FROM BUS_ROUTE_STOPS BRS INNER JOIN BUS_ROUTE BR ON BRS.Route_number = BR.Route_number INNER JOIN BUS_STOP BS ON BS.Stop_ID = BRS.Stop_ID WHERE BRS.Route_number = \'" + A + "\';")
print(baseTable)

routes = db.execute_command("SELECT BR.Route_number FROM BUS_ROUTE BR GROUP BY BR.Route_number")
db.close()


