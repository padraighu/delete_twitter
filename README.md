# Delete Your Tweets

Scripts to automatically delete your tweets. Recommended to be run in a docker container.

[Twitter API access](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) is required.

### How to run

```sh
docker build -t delete_twitter .

docker run \
-e apikey="..." \
-e apikeysecret="..." \
-e bearertoken="..." \
-e accestoken="..." \
-e tokensecret="..." \
-e screen_name="..." \
delete_twitter 20220801
```
