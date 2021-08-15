import subprocess

# run a simple command
subprocess.run('ls')

# similar to run simple command to avoid any errors
subprocess.run('ls', shell=True)

# also if we set shell=True we can pass in an entire command as string
subprocess.run('ls -la', shell=True)

# if we wanna run the same command as above we must pass a list
subprocess.run(['ls', '-la'])

# we need to try and capture the standard-out here
c1 = subprocess.run(['ls', '-la'])
print(c1)

# we can check the arguments that we gave as commands
print(c1.args)

# we can also check the return codes, these tells us whether we got any errors or not
# normally code=0 means no error - everything went smoothly
print(c1.returncode)

# we can also grab standard out as well
print(c1.stdout)  # we get none bcz
# the subprocess send all of the output to the console and not here
# to get it we need to capture it here too
c2 = subprocess.run(['ls', '-la'], capture_output=True)
# when u do capture_output=True no output is printed out while we execute this python script, everything is captured in c2 variable itsel
print(c2.stdout)
# the output is not formatted well bcz the output is captured as bytes
# we could decode those bytes and convert them to string
print(c2.stdout.decode())
# another way to do this is to set text attribute to true
c3 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(c3.stdout)

# when we set capture_output=True, it sets standart out to subprocess.pipe this allows us to capture those values
# capture_output=True same as
c4 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(c4.stdout)  # we get the same results

# What if we wanna log the output in a file
with open('log.txt', 'w') as f:
    c5 = subprocess.run(['ls', '-la'], stdout=f, text=True)
    # look at the file for results

# Let's look at what to do when we get an error
# when the external command fails python doesn't give us error but it will provide us with appropriate error code
c6 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
# we got a code=2 which means error bcz the code is other than 0
print(c6.returncode)
# we wanna know what that error is
print(c6.stderr)

# we want python to throw an exception when the command fails to be executed, what do we do?
# we add check attribute
# c7 = subprocess.run(['ls', '-la', 'dne'],
#                     capture_output=True, text=True, check=True)

# what if we don't wanna care if the command is executed successfully or not
c7 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL, text=True)
print(c7.stderr)  # we will get none, eventhough command isn't successful

# what if we wanna take output of one command and use it as input to another
c8 = subprocess.run(['cat', 'log.txt'], capture_output=True, text=True)
print(c8.stdout)  # we have go the contents of the file printed out
c9 = subprocess.run(['grep', '-n', 'run'],
                    capture_output=True, text=True, input=c8.stdout)
print(c9.stdout)
