# Python

## Creating a Lambda Layer for use in AWS

In this example we'll create a layer for requests

```python
python3 -m venv venv
source venv/bin/activate
mkdir python  
pip install requests -t python  
zip -r requests.zip python
```

Next, go to AWS lambda and upload your layer.
Select the runtimes (python 3.xxxx) and architectures.

In the lambda CLI, go to add layer and select it from the list.
In the lambda-code you can now use the regular

```python
import requests
```

When you print have dumped a plain python dict and now want to use something
like jq to parse it, you have to work your way around False vs false, None
vs null ect.

```
echo "{'foo':False, 'bar':None, 'foobar': True}" |sed -e 's/False/false/g' -e 's/True/true/g'  -e 's/None/null/g' | tr "'" '"'  | jq

{
  "foo": false,
  "bar": null,
  "foobar": true
}

```