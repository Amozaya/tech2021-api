# What is API?

API (application programming interface) - is a set of defined rules that enable different applications to communicate with each other.

![API Diagram](resources/API_Diagram.png)


API architecture could be explained in terms of client and server. The application that user is using acts as a client as it sends a request, and the application that responds is called the server.
For example, the weather software system contains daily weather data, and the weather app on the phone will communicate with the software via API to show daily updates. In this example, weather app is a client and weather software database is a server.

API benefits:
* Improved collaboration - enables communications between remote applications
* Accelerated innovation - API offers flexibility, allowing companies to make connections with the new business partners, offer new services to their existing marked, and access new markets
* System security - API separates the requesting application from the infrastructure of the responding service, and offers layers of security between the two as they communicate
* End-user security and privacy - it also adds a layer of protection for a personal user. When a website requests a user's location, which is provided via a location API, the user can then decide whether to allow or deny this request

### REST API
REST stands for Representational State Transfer. It defines a set of functions like GET, PUT, DELETE, etc. that clients can use to access server data. Clients and severs exchange data using HTTP.

The main feature of REST API is statelessness, which means that servers do not save client data between requests.

In order for an API to be considered RESTful, it has to conform to these criteria:
* A client-server architecture made up of clients, servers, and resources, with requests managed through HTTP.
* Stateless client-server communication, meaning no client information is stored between get requests and each request is separate and unconnected.
* Cacheable data that streamlines client-server interactions.
* A uniform interface between components so that information is transferred in a standard form.
* A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved the retrieval of requested information into hierarchies, invisible to the client.
* Code-on-demand (optional): the ability to send executable code from the server to the client when requested, extending client functionality. 

## What is HTTP
HTTP stands for Hyper Text Transfer Protocol
Internet is about communication between web clients and servers, and it can be done by sending HTTP Requests and receiving HTTP Responses.

Communication between clients and servers:
1. A client (a browser) sends a HTTP request to the web
2. A web server receives the request
3. The server runs an application to process the request
4. The server returns an HTTP response (output) to the browser
5. The client (the browser) receives the response

#### HTTP Request Structure

![HTTP_request Diagram](resources/HTTP_request.png)

HTTP Request in general divided in 3 parts:
1. A request line
2. A set of header fields
3. A body, which is optional

*Request line:*

In the request line we usually place HTTP Method to be used and the URL of the request:
* Request method indicates the method to be performed on the resource by the given Request-URL
* Request-URL is a Uniform Request Identifier and identifies the resource upon which to apply the request

*Request header:*
The request header field allows the client to pass additional information about the request, and about the client itself, to the server.

*Request body:*
The Request body is where we put the additional information that we are going to send to the server.
In the body of the request we are free to place virtually whatever we want(username, passwords, answers to survey, etc.)


#### HTTP Response Structure

![HTTP_response Diagram](resources/HTTP_response.png)

HTTP Response also has its own structure and divided in 3 parts:
1. A status line
2. Header
3. A body, which is optional

*Status line:*
A status line shows the request status, if it was successful, if there was an error, or if it is required that we take some type of action.
It is also known as Status Code, and usually if you receive a status code "200", it means that request was successful. 

*Response header:*
The Header field is just like Headers in request.

*Response body:*
The Server has an option to send a body with the data that it wants to transmit to us.



### HTTP Methods
HTTP defines a set of request methods to indicate the desired action to be performed for a given resources. They are also can be referred to as HTTP verbs.
5 HTTP verbs:
* GET - the GET method requests a representation of the specified resource. Requests using GET should only retrieve data
* POST - the POST method submits an entity to the specified resource, often causing a change in state or side effects on the server
* PUT - the PUT method replaces all current representations of the target resource with the request payload
* DELETE - the DELETE method deletes the specified resource
* PATCH - the PATCH method applies partial modifications to a resource

### Caching

In computing, a cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location. 
Caching allows you to efficiently reuse previously retrieved or computed data.