### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
   PostgreSQL is a relational database management system that is used to store and query data of many different types.
- What is the difference between SQL and PostgreSQL?
   PostgreSQL is a bit more advanced than traditional SQL, and it is an Object based RDBMS, as opposed to a standard RDBMS.
- In `psql`, how do you connect to a database?
   For me, I just type "psql postgres", but I know there was a different way in the course. I set up Postgres long before I started the course.
- What is the difference between `HAVING` and `WHERE`?
   The WHERE clause is applied to rows, whereas the HAVING clause is applied to groups of rows.
- What is the difference between an `INNER` and `OUTER` join?
   An inner join is the typical join that we do, and will only fetch information that is present in both tables that are being joined. An outer join will fetch information from both tables, depending on if it is a LEFT OUTER or RIGHT OUTER join.
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
   A LEFT OUTER join includes the rows from the table on the left, even if there is no match in the table on the right. A RIGHT OUTER join does exactly the opposite.
- What is an ORM? What do they do?
   An ORM is an Object Relational Mapper that allows you to write to and query a database, using object oriented programming. They are usually part of a library, such as SQLAlchemy.
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
   The main difference is that AJAX is asynchronous, which allows other processes to continue running, and Python requests is not. Also, AJAX returns JSON by default, but Requests does not.

- What is CSRF? What is the purpose of the CSRF token?
   CSRF is Cross Site Request Forgery. The purpose of the token is to prevent bad actors from taking your form and using it to submit malicious data.
- What is the purpose of `form.hidden_tag()`?
   "form.hidden_tag()" allows the CSRF token to be present in the form, but hidden from the display in browser.
