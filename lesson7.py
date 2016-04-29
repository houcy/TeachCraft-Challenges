from mcpi import minecraft
import time

server_address = "199.96.85.3"
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

#We first need to get our player ID, so we can focus on just listening to messages posted by us in chat
my_id = mc.getPlayerEntityId(my_player_name)

print "Script started! Type in 'hi' or 'testing' in minecraft chat to activate. Hit command (or control) + C in your terminal to stop."

#Watch for chat messages
while True:

    #For each chat message since the last time we checked...
    for chatpost in mc.events.pollChatPosts():

        #Was the chat message sent by me?
        if chatpost.entityId == my_id:

            #if so, let's do something!
            if chatpost.message.lower() == "hi":
                mc.postToChat("Hello right back at you!")

            elif chatpost.message.lower() == "testing":
                mc.postToChat("123")

    time.sleep(.1)


#CHALLENGE 1
# Modify the script above, and add a chat trigger called "shield" that builds a glass shield "building"
#   all around you, making it so nothing can attack you but you can still see. Hint: Refer to lesson5

#CHALLENGE 2
# Modify the script above, and add a chat trigger called "nuke" that spawns several TNT around you.
#   You'll also need to spawn redstone torches next to the TNT to activate it. (Try under)
#   Make sure you spawn the TNT far enough away from you it doesn't kill you, but close enough it can
#   take out your enemies!

#CHALLENGE 3
# Modify the script above, and add a chat trigger called "jail" that puts your opponent into a bedrock prison.
#   This is similar to the "shield" spell, with a few differences.
#   1) Instead of using glass, use bedrock.
#   2) Instead of centering it around YOUR position, you need to center it around your OPPONENT's position!
#   3) Instead of a single trigger word, you need two. E.g. instead of just "shield" you need "jail seanybob"
#
#   When thinking about how to approach this, think of the flow of data. You're passing in your opponent's
#   name via a parameter, so you'll need to extract that. Now, you have your opponent's name, but the getPos()
#   function doesn't have a name parameter! Try thinking back to what you did earlier in the script to create
#   a connection to the minecraft server for a specific name.