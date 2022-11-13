import twitter
import arrow
import argparse
import os


apikey = os.getenv("apikey")
apikeysecret = os.getenv("apikeysecret")
bearertoken = os.getenv("bearertoken")
accestoken = os.getenv("accestoken")
tokensecret = os.getenv("tokensecret")
screen_name = os.getenv("screen_name")


def delete_tweets(api: twitter.Api, date_since: str):
    my_tweets = api.GetUserTimeline(api.GetUser(screen_name=screen_name).id, count=1000)
    cutoff = int(float(arrow.get(date_since, "YYYYMMDD").format("X")))
    to_delete = [t.id for t in my_tweets if t.created_at_in_seconds > cutoff]
    
    for d in to_delete:
        api.DestroyStatus(d)


def delete_likes(api: twitter.Api):
    my_likes = api.GetFavorites(api.GetUser(screen_name=screen_name).id, count=5000)
    to_delete = [l for l in my_likes]

    for d in to_delete:
        try:
            api.DestroyFavorite(d)
        except:
            continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI to delete tweets.")
    parser.add_argument(
        "--date_id", type=str, nargs="?", help="Delete tweets since date"
    )
    args = parser.parse_args()
    api = twitter.Api(
        consumer_key=apikey,
        consumer_secret=apikeysecret,
        access_token_key=accestoken,
        access_token_secret=tokensecret,
    )
    delete_tweets(api, args.date_id)
