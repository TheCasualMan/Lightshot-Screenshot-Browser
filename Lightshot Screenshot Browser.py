import random
import time
import webbrowser

num = 10
while True:
	for x in range(num):
		chrs = 'abcdefghijklmnopqrstuvwxyz1234567890'

		link_end = (''.join(random.choices(chrs, k=6)))
		print(link_end)
		webbrowser.open_new_tab(f"https://prnt.sc/{link_end}")
		time.sleep(3)