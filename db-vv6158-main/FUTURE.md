## Reactions

Firstly to implement this we need to change our messages and community_channels table. Messages table can add whether a message has a reaction or not. These messages would then be joined to a new reactions table for which I can make helper methods that, given (sender,message, reaction), can add or change a reaction to a text. 

API methods that insert messages into messages or community_channels would need to change to include reaction. 


## Threaded Conversations

We would definitely need a threaded conversations table that is joined to the community_channels table and messages table. 
We would need API methods to insert new messages to the threaded conversation. We could add a key to keep track of the replies and we can use the keys to access messages. Existing API methods probably wont need to change unless we want a yes/no for whether it is a threaded conversation, but that likely wont need to happen, because we have other functions that help us with that. 


