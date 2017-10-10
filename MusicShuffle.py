import webbrowser
import random

new=2;
a = 280000000
b = 306000000
c = random.randint(a,b)


url="https://api.soundcloud.com/tracks/"+str(c)+"/stream?client_id=3aa6254cb799019fb9d7d115726f8805";

webbrowser.open(url,new=new);