# dojo

> Backend for [tunes.ninja](https://tunes.ninja/) features such as syncing playlists, controlling playback and linking services.


***

## Setup


## Required services
- Mongo
  - You must specify the database name, port, host in the configuration.
- Redis 
  - You must specify host and port.
***

### Celery Setup 

Celery can be initialized from ```dojo.background.celery_configuration.background```. Mongo and Redis **must** be reachable in order to process background tasks. 



### HTTP API Setup

Dojo can be started using uvicorn from the entrypoint of ```dojo.rest.main:application```


***

## Intergrating with services

### Apple Music:
A valid Team ID and Developer Token. You can retrieve these keys from Apple.

**Note**: A valid frontend must be available to login a user through Apple Music. Once retrieving an authenticated API key from MusicKit, you'll need to pass this to the API.


### Spotify
A valid Client ID, Client Secret and Redirect URI. You can retrieve these keys from the Spotify Developer Console.

**Note**: A valid frontend callback URL must be provided! Users will be redirected to this site when successfully linking their Spotify Account