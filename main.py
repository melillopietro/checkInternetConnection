import urllib.request
def connect():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
print(" ")
print("Test di connessione ad internet in corso...")
print( 'connesso ad Internet ' if connect() else 'non connesso ad Internet!' )