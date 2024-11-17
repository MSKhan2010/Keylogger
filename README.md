Malware, one of the most dangerous threats to our everyday use of devices and the most engaging tool used by black hat hackers to absolutley annihilate and create unrecoverable
losses to companies, businesses, websites and computers. 

Ever since the creation of Computers, we have had many groundbreaking incidents involving malware, targeted at companies as big as NHS. We saw
the famous WannaCry ransomware outbreak in 2017 which led to companies like the NHS, Honda and Nissan facing data loss and bitcoin money in return of the data.

However, we're not going too deep into ransomware attacks. There are many sorts of malware out there, ransomwaree (as mentioned before), adware, worms and other viruses.
The type of malware we're looking at right now is Spyware specifically a simple keylogger.
When you open this github repository you'll see three folders, `tcp`, `src` and `Flask`. We'll go through each of the folders one by one. First when you open the `src` folder,
you'll realise that there is a `keylogger.py` script, here you can try tell what the script is going to do if you are familiar with python.

If not, what this script will do is that when ran through the command prompt/powershell (if on windows), mac terminal (if on macOS) or the Linux terminal (if on Linux) `python3 keylogger.py` 
or (if on linux or mac),  `chmod +x keylogger.py; ./keylogger.py`, it will listen for any keyboard input by the user, whether thats outside the program itself
or in a game, or in a web browser, whatever you've typed whether thats a password, url or username will be captured. Now, to review the captured input press `esc`, 
you will all of a sudden notice a `keylog.txt` file and when opened you will see every key pressed from this, you could make out passwords and activity e.t.c.
Isn't that amazing?

Now, if this was done by a 'real' hacker they would take it a step further and make a keylogger script so it tells the user which files, applications and other things the user
have opened, they may also make it so that when the user for example types a suspected password, it may come back notified to the user. However, although our keylogger is okay,
there is still one problem, 
This wouldn't work if you were trying to hack someone else remotley, **it will work in some use cases** for example, you give your device to someone you know,
then they use it to for example, go on their social media by logging in, that would work and tell you the keys they pressed which you will maybe find the password or username
they put in through the keylog.txt file however if you send it to someone you wont recieve the keys, as the `keylog.txt` file is made on **their device**.

However, **not to worry**, that's why we have the `tcp` folder from earlier, when you open this folder, you will see two python scripts, a `server.py` and a `client.py`
the **server** is where it will listen for a connection, and when the **client connects**, the 'hacker' let's say can now receive the output onto its console.
To get this working first **run** the `server.py` script, **powershell/cmd**: `python3 server.py` or in **mac/linux terminals**: `chmod +x server.py; ./server.py`
You will receive the following message, `Listening on {IP}{PORT}` Please remember, if you want to change the IP addresses, change the IP or Port variables if needed.

Now you've got a server running, now with the `client.py` you could either give it to a friend,family member e.t.c **with explicit permission** with a computer
I would recommend converting it into an executable using pyinstaller because not all systems have Python on their computers. Or you could just run the `client.py`
yourself, on another terminal window, because keeping the server up is important. Next, run the `client.py` script, nothing happened? However if you look into your
server console, You will receive a message, `Connection from {IP}:{PORT}` this means the connection was successfull. Now, whatever the client types in, the keys will come in live
output to the server console, isn't that amazing? And what's even scary easy is that the target won't even know. Now, there are some loopholes in this, many firewalls,
antivirus systems e.t.c can detect such activity and **immediatley** delete the file, and sometimes firewalls may block incoming connections in fear of
common attacks like reverse-shells. However, this is still a very reliable source if you want to attack someone from local network users and other remote networks.
And can have a really big effect.

The Flask folder is not finished yet, I would love to get some assistance, as it involves web devlopmenet using Node and Javascript, which I am not familiar with. In the end
please do remember to stay safe and always stay ethical no matter what.










