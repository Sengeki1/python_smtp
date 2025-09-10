# SMTP

SMTP (Simple Mail Transfer Protocol) is the standard protocol used to send emails across the internet.
It acts like a *digital postman*, making sure your message leaves your computer, passes through your email provider’s server, and arrives at the recipient’s mail server.

* SMTP only handles *sending and relaying* messages.

* To read messages later, other protocols like *IMAP* or *POP3* are used.

* It follows a step-by-step conversation: the client says hello, provides sender and recipient information, sends the email data, and then closes the connection.


In this project, SMTP is demonstrated in two ways:

* Sending a *simple email* (no attachment)

* Sending an *email with attachments*


Official SMTP Documentation: [RFC 821 – Simple Mail Transfer Protocol](https://datatracker.ietf.org/doc/html/rfc821)

Python guide to sending emails: [Mailtrap – Python Send Email Tutorial](https://mailtrap.io/blog/python-send-email/)