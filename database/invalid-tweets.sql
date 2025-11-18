# Use the LENGTH(content) function to calculate the character count of each tweet.

SELECT tweet_id FROM Tweets 
WHERE LENGTH (content) > 15;