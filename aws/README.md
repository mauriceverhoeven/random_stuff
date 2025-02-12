# aws commands

## listing files in your s3 bucket

```
aws s3api list-objects-v2 --bucket "YOUR_BUCKETS_NAME" --max-results 10
```

will return a json something like this:

```
{
    "Contents": [
        {
            "Key": "006g82Reci3E/af306e20-38a8-11eb-b49d-f9b9b1a64443/bar.smil",
            "LastModified": "2022-07-29T15:24:03+00:00",
            "ETag": "\"63d4a1cebf89563a3671003f5e5dbb4e\"",
            "Size": 404,
            "StorageClass": "STANDARD"
        },
        {
            "Key": "006g82Reci3E/af306e20-38a8-11eb-b49d-f9b9b1a64443/foo.mp4",
            "LastModified": "2022-07-29T15:24:03+00:00",
            "ETag": "\"3c29a000953a62bb17d36fc4b506f010\"",
            "Size": 23653866,
            "StorageClass": "INTELLIGENT_TIERING"
        }.... etc

    ],
    "NextToken": "eyJDb250aW51YXRpb25Ub2tlbiI6IG51bGwsICJib3RvX3RydW5jYXRlX2Ftb3VudCI6IDEwfQ=="
}

```



## list json or vtt files in your s3 bucket
if you play around with the filters you should be able to only get the
output you want.
I do believe that the filtering is done client-side as it takes forever even
if you filter the content to start with a particular key :/ 


```
aws s3api list-objects-v2 --bucket "YOUR_BUCKETS_NAME" --query "Contents[?ends_with(Key, '.json') ||  ends_with(Key, '.vtt')]
```

