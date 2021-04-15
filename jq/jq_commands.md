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

```cat sample.json| jq -c  ".datapoints[0]| keys" | tr -d '"' | sed -E s'/,/, ./'g | sed -E s'/\[(.+)/jq -c  ".datapoints[] | [.\1 | @csv"/' 
```

eg: 
```jq -c  ".datapoints[] | [.id, .prop1, .prop2, .prop3, .prop4] | @csv" 
```

```cat sample.json| jq -c  ".datapoints[] | [.id, .prop1, .prop2, .prop3, .prop4] | @csv"
"160,228,5,100,19966"
"161,228,5,200,20066"
```