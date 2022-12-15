# Sensium Connect GraphQL API Example (Python)

The included Python3 `example.py` logs into Sensium Connect and makes some queries using the GraphQL API, then
logs out again.


## Setup

Install the required dependencies by running:

```bash
$ pip install -r requirements.txt
```


Create a Personal Access Token in the Sensum Connect UI.


## Running

```bash
$ python example.py <TOKEN>
```

Where `TOKEN` is the personal access token you created earlier.

This should output something similar to the following:
```
Logging in... Session abcdef-0123456-abcdef
Executing query "{ me { name } }"
{
	"me": {
		"name": "API User"
	}
}
Loggout out... OK
```

If `TOKEN` is incorrect you will see this output:
```
Logging in... FAILED (Invalid personal access token)
```


# More Information

For additional information, please see the following:

 * https://graphql.org/learn/
 * http://apidocs.sensiumlabs.com

