## What is YAML

1. YAML is an indentation based markup language.

## Set of elements forming a yaml file

### Scalars
1. number-value: 42
2. floating-point-value: 3.14
3. boolean-value: true
4. string-value: "Hi"
5. unquoted-string-value: Hello World

### Lists

Lists are collection of elements:

Example:

~~~~
fruits:
    - Apple
    - Tomato: It is actually debated
    - Mango
~~~~

Corresponding json structure:

~~~~
{
    "fruits": 
    [
        "Apple",
        {
            "Tomato": "It is actually debated",
        }
        "Mango"
    ]
}
~~~~

### Dictionaries

Dictionaries are collection of key-value pairs:

Example:

~~~~
animals:
    Labrador: Dog
    Tiger: Cat
    Plane cat: Cat
    Jersey: Cow
~~~~

Corresponding Json structure:

~~~~
{
	"animals": 
    {
		"Labrador": "Dog",
		"Tiger": "Cat",
		"Plane cat": "Cat",
		"Jersey": "Cow"
	}
}
~~~~

### One single complex example

~~~~
execution:
- concurrency: 10
  hold-for: 5m
  ramp-up: 2m
  scenario: yaml_example
  
scenarios:
  yaml_example:
    retrieve-resources: false
    requests:
      - http://example.com/

reporting:
- module: final-stats
- module: console

settings:
  check-interval: 5s
  default-executor: jmeter

provisioning: local
~~~~

Corresponding JSON

~~~~
{
	"execution": [
		{
			"concurrency": 10,
			"hold-for": "5m",
			"ramp-up": "2m",
			"scenario": "yaml_example"
		}
	],
	"scenarios": {
		"yaml_example": {
			"retrieve-resources": false,
			"requests": [
				"http://example.com/"
			]
		}
	},
	"reporting": [
		{
			"module": "final-stats"
		},
		{
			"module": "console"
		}
	],
	"settings": {
		"check-interval": "5s",
		"default-executor": "jmeter"
	},
	"provisioning": "local"
}
~~~~
