I'd like to put the answer right at here because this thread is on top of the google search ''ts-node max-old-space-size"

node -r ts-node/register --max-old-space-size=3049
Update
If you are running with os.arch() === 'ia32', the max value you can set is 3049

under my testing with node v11.15.0 and windows 10

if you set it to 3050, then it will overflow and equal to be set to 1.
if you set it to 4000, then it will equal to be set to 51 (4000 - 3049)