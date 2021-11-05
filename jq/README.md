# JQ commands

on a "flat" json like -->
``` {
	"datapoints": [{
			"id": 160,
			"prop1": 228,
			"prop2": 5,
			"prop3": 100,
			"prop4": 19966
		},
		{
			"id": 161,
			"prop1": 228,... 
```

use the keys from to 'auto-create' with some et-sed-tra to create the output to csv command

```
cat sample.json| jq -c  ".datapoints[0]| keys" | tr -d '"' | sed -E s'/,/, ./'g | sed -E s'/\[(.+)/jq -c  ".datapoints[] | [.\1 | @csv"/' 
```

which results in:  
```
jq -c  ".datapoints[] | [.id, .prop1, .prop2, .prop3, .prop4] | @csv" 
```

and can be used :
```
cat sample.json| jq -c  ".datapoints[] | [.id, .prop1, .prop2, .prop3, .prop4] | @csv"
"160,228,5,100,19966"
"161,228,5,200,20066"
```

selecting stuff
```
echo '{"files": [{"fileName": "FOO","md5": "blablabla"}, {"fileName": "BAR","md5": "alaldlafj"}]}'  | jq '.files[] | select(.fileName=="FOO") '
{
  "fileName": "FOO",
  "md5": "blablabla"
}
```

using it on har files:

```
jq '.log.entries[].request | {method,url}' $1 | jq 'if .method=="GET" then .url else "" end' | grep -Eo "http(s?)://([^/]+)./" | sort | uniq
```

```
cat browsertime.har| jq '.log.entries[]| {method: .request.method, status: .response.status, size: .response.headers[] | select(.name | contains("content-length")).value, url: .request.url, csp: .response.headers[] | select(.name | contains("content-security-policy")).value?, contenttype: .response.headers[] | select(.name | contains("content-type")).value  } ' | grep status
```

```
cat player.theplatform.eu.har | jq '.log.entries[] |select(.request.url | startswith("https://vod.tst1.talpatvcdn.nl/")) | {url: .request.url, size: .response.content.size}'
```