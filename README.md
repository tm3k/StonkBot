# StonkBot 99% finished. Just need to make it look pretty and export the data to an infographic instead of reading it manually from console. 
# You can change the signals it generates to only when price is below bbands by making the following change:

elif i > 1:
                trade_signal.append('XXXXXXX'),
                
            #CHANGE TO#
            
elif i > 1:
                trade_signal.append(''),
                
# The idea behind the bot is as follows: In an uptrend on any asset, there will be dips, those dips sometimes mark an exact bottom when %b goes below 0(outside below bbands). This only works in an uptrend. 

# If you want to use it to short you need to do the inverse. Only Sell when price goes above the bbands IN A DOWNTREND. (above 1 on %b)

# You need to manually determine trend, dont buy the dip in a downtrend. Need to figure out code for determining trend to further filter the results the bot generates. 
