## DataSet

App development using [Tornado](https://www.tornadoweb.org/en/stable/), a Python Framework really similar to [Django](https://www.djangoproject.com/), 
and a SQL as [PostgreSQL](https://www.postgresql.org/s). We decided to follow a [DDD](https://justdigital.agency/que-es-domain-driven-design-ddd/)
pattern, in order to build scalable code.

* On one hand we have the repository folder, where we have the responsibility to connect our backend with our DB, 
in this case Postgresql. If we want to change to a No-SQL DB, we just have to implement those files and our app won’t know it.
* On the other hand, we have the handlers folder, which receives all of the request from endpoint.
* In the services folder we have every business rule, in this case, Mastermind rules.
* And in the last instance we have the Models folder, where we have entities which represent different object of our system and it helps to have a clear code.

* For the Models, we use a ORM representation to help us to communicate ourself with the database, and also
will be easier to filter, sort and group by. Everything under [SQLAlchemy](https://www.sqlalchemy.org/).

* For the database, we used [ElephantSQL](https://www.elephantsql.com/) just to skip waste time on the docker configuration,
and also to skip to install it in our system. (this is just for the test).

***Note:*** To have a clear registry, we have pushed directly into master. The correct and **mandatory** way is create one branch for each feature and merge it into Develop branch.
 Once we test it, we should merge it into master (if we follow [Git Flow](https://es.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) methodology)

## Use
For build our dockers on localhost or on deploy, we created a Makefile file with the common docker commands.
+ To build and run dockers we have to execute: `make start`
+ To stop these containers: `make stop`
+ To run unit tests: `make test`

## Containers

1. For our app we will use Python 3.6.7 where we will install Tornado (`/api`).
2. [Nginx](https://www.nginx.com/) image where we will have configured as a reverse proxy, to deploy it on any server and test it. 
If we run it on a server, we will have to access through our IP machine with the current port, in this case 80, where Nginx is listen our request.
3. [Swagger](https://swagger.io/) image to document our different endpoints. (`/`)

## Use of our App.

To have a clear request, we will use the POST method and we will write in our body what fields we
want to filter, sort or group. Always using JSON as way to give and receive any data.

```json
{
	"filter": {
		"country": "spain",
		"os": "ios"
	},
	"group": ["channel", "country"],
	"sort": ["impressions"]
}
```


## The Future of our App Development.
* [Swagger](https://swagger.io/) for our API documentation.
* Continuous Integration / Continuous Delivery using [GitLab CI/CD](https://about.gitlab.com/product/continuous-integration/) native facilities (if we host it on GitLab).
* [Ansible](https://www.ansible.com/) Script for the automation and provisioning.

*Author: Víctor Vallecillo Morilla email: viictorvallecillo@gmail.com*
