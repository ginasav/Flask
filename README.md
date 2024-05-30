# Flask
Flask x Python

Flask is a lightweight and flexible web framework for Python. It is designed to make it easy to build web applications quickly and with minimal code. Flask is known for its simplicity, versatility, and ease of learning, making it a popular choice among developers for building web applications, APIs, and more.

Key features of Flask include:

- Simple to Use: Flask is designed to be easy to use and understand. Its simple and intuitive API allows developers to get started quickly with building web applications.

- Minimalistic: Flask is lightweight and unopinionated, meaning it provides just the essentials for building web applications without imposing any specific architecture or design patterns. This gives developers the freedom to structure their applications as they see fit.

- Extensible: Flask is highly extensible, allowing developers to add additional functionality through Flask extensions. These extensions cover a wide range of features such as authentication, database integration, form validation, and more.

- Jinja2 Templating: Flask uses the Jinja2 template engine, which allows developers to easily create dynamic HTML content by combining HTML templates with Python code.

- Built-in Development Server: Flask comes with a built-in development server, making it easy to test and debug applications locally before deploying them to production servers.

- Werkzeug WSGI Toolkit: Flask is based on the Werkzeug WSGI toolkit, which provides low-level utilities for handling HTTP requests, routing, and other web-related tasks. This allows Flask to remain lightweight while still providing powerful functionality.

Overall, Flask is a popular choice for developers who want to build web applications quickly and efficiently, without being tied down by unnecessary complexity or rigid conventions. Its simplicity and flexibility make it suitable for a wide range of use cases, from simple hobby projects to large-scale production applications.


<h3> Differenze tra GET e POST request </h3>

<h4> GET Request </h4>

  <b> Purpose: </b>
      GET requests are used to retrieve data from a server.

  <b> Data Transmission: </b>
      Data is sent as part of the URL. For example: http://example.com/search?query=python.
      The parameters are appended to the URL as a query string.

  <b> Visibility: </b>
      Data is visible in the URL, which means it can be bookmarked or shared.
      It is also stored in the browser history.

  <b> Size Limit: </b>
      There is a limit to the amount of data that can be sent because URLs have length restrictions.

  <b> Idempotency: </b>
      GET requests are idempotent, meaning multiple identical requests will have the same effect as a single request.

  <b> Use Case: </b>
      Suitable for actions that do not change the state of the server. Examples include searching, reading data, and accessing pages.

<h4> POST Request </h4>

 <b> Purpose: </b>
      POST requests are used to send data to a server to create or update a resource.

 <b> Data Transmission: </b>
      Data is sent in the body of the HTTP request, not as part of the URL.

  <b> Visibility: </b>
      Data is not visible in the URL, making it more secure for sensitive information like passwords.
      It is not stored in the browser history.

  <b> Size Limit: </b>
      Generally, there is no size limit on the data sent, making it suitable for larger amounts of data.

 <b> Idempotency: </b>
      POST requests are not idempotent. Multiple identical requests may result in different outcomes, such as creating multiple resources.

  <b> Use Case: </b>
      Suitable for actions that change the state of the server, such as submitting forms, uploading files, and creating new resources.
