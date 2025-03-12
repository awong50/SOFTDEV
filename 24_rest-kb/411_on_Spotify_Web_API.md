Collected Knowledge & Wisdom on
# Spotify Web API

## Provides:
The Spotify Web API allows users to access Spotify's musig catalog, user playlists, playback controls, and other music-related features. In addition to the name and image of songs, it provides useful metadata for release dates, album types, and more! 



### Pain factor: _
5

### Key Provisioning:     

- A Spotify Account is required to use the Web API (https://open.spotify.com/)
- Start by creating an app in the Spotify Developer Dashboard
    - Redirect URls are where users are redirected after authentication success (For testing purposes, it is common to use localhost)
- Client ID and Client Secret: Accessed after app is created and are vital to the creation of Authentication Keys | [Guide](https://developer.spotify.com/documentation/web-api/concepts/apps)
- Two types of Auth Keys: Access Token (short lived) and Refresh Token (used to get new access tokens - only used in specific OAuth Flows)
- OAuth Authorization Flows: Different authentication methods for differnet use cases | [Guide](https://developer.spotify.com/documentation/web-api/concepts/authorization)



### Quotas:
- Dynamic Rate Limit (~180 requests per minute): Determined by how many requests are sent in a 30 second window; If exceeded, it will begin returning 429 error responses from the API
- Access Token lasts for an hour before requiring a refresh of token

---

## The Good:
- Well documented with many examples and tutorials
    - Teaches you programming jargon like client credentials flow
- Full control over retrieving and altering personal information in your account (creating/deleting playlists, favoriting, playing songs, etc)
- Established company, which means less bugs and more security

## The Bad:
- Very complicated code (for security) to access the API
- Rate-limiting (depending on the use case)
- Some features (like the web player node package) are locked behind Premium (which is $10 a month)


## The Ugly:
- How-To Guides and code blocks are in JS and Typescript, which is terrible for us newbie Flask users 


**Location:** https://developer.spotify.com/documentation/web-api

---

Accurate as of (last update):    2024-11-21

Contributors:

Aidan Wong, pd4  
