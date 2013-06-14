RFIDAUTH

Authenticate yourself using RFID tags and your phone.

The concept works as follows:

The system has three components. An app on your phone/tablet which can write
and read RFID tags, a server which is publicly accessible with a browser 
through SSL, and a client on the target system that will do an action upon 
authentication (like unlocking a screen, opening a door, or whatever you 
think of.)

The app and the client/device need to be registered and linked to a username.
Finally, the android app will be used to write a special URL on the tag,
which will open the app and do a request for that URL with authentication 
tokens. The webserver will then queue the registered action for the client or
device. The client or client will poll the server for queued actions. When
the client picks up on the action, it will fetch it from the server and 
execute it.

The format and installation instructions will follow when I have something
that halfway works.

