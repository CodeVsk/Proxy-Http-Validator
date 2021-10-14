import requests, time, threading

thread = 5
proxys=None

target = input("Link (http://example.com  or https://example.com): ")
timeout = input("Timeout (5,10,15): ")

r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
proxys = r.text.split('\n')

def chunker_list(seq, size):
    return (seq[i::size] for i in range(size))

def recycler(proxylist,id_):
    for x in proxylist:
        try:
            r = requests.get(target, proxies={"http":"http://"+x}, timeout=int(timeout))
            if r.status_code == 200:
                print("\33[1m \33[32m[PROXY ONLINE]\033[0m \33[37m","http://"+x)
        except:
            pass

data=list(chunker_list(proxys, thread))

for i in range(0,thread):
    t = threading.Thread(target=recycler, args = (data[i],i))
    t.start()