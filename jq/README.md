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

if you want to create a csv (the first bit of jq is only to select the proper parts i needed for the sample.
You can probably do this in one go also but would make the actual bit less usefull.
```
cat sample.json | jq '.datapoints[] ' | jq -r -s '. | (map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[]| @csv'
"id","prop1","prop2","prop3","prop4"
160,228,5,100,19966
161,228,5,200,20066
162,229,5,300,20166
163,229,5,400,20266
164,230,5,500,20356
165,231,5,500,20466
166,231,5,700,20566
167,232,5,764,20650
168,232,5,964,20750
169,233,5,964,20850
170,233,5,1064,20950
171,234,5,1164,21050
172,234,5,1264,21150
1210,0,0,0,0
```
