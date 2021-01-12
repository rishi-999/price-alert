from models.alert import Alert

alerts=Alert.all()
for Alert in alerts:
    Alert.load_item_price()
    Alert.notify()

if not alerts:
    print("no alerts have been created. Add an item and an alert to begin!")