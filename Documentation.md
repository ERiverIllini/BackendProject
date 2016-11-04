#GET /api/choice
###Gets information about this name

Request Parameter | Value Type | Value
------------------|------------|----------------------------
Name | string | Name of a person or song to be searched on Twitter, Spotify, and Wikipedia

##Response
###This method returs a JSON object containing the following key:value pairs

Response | Value Type | Value
---------|------------|-----------------------------
Top Track in Spotify, Tweets, and Wikipedia text | dict(spotify->string, twitter->string, wikipedia->string) | The dictionary has three key:value pairs where the keys are the various sources and the values are the information from the respective sources.  
