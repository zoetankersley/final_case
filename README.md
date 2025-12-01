# README- Zoe Tankersley

**Project Title: Motivational Quote API**

## **1) Executive Summary**

**Problem:** Day-to-day life can be stressful or draining, and sometimes people need a quick mood boost to get them back on track. This project provides an easy way for the user to get a motivational quote catered to their needs. It is meant to help any student, worker, or person looking for some inspiration.

**Solution:** The Motivational Quote API allows users to access a library of inspirational quotes through a user-friendly web interface. Users are prompted with a dropdown menu where they can either request a random quote, or filter quotes by their desired category such as “growth,” “confidence,” or “mindset.” Once selecting a category from the dropdown menu, users are instantly presented with a matching quote, as well as its author. This setup demonstrates how backend APIs and frontend interfaces can work together to provide users with an easy-to-use, uplifting website.

## **2) System Overview**

**Course Concept(s):** The main course concepts I used for this project were Flask API and containerization with Docker. I used Flask to build a lightweight API that handles routes and outputs motivational quotes. I worked with JSON data handling to load, filter, and serve the quote data. I included a simple frontend using HTML to allow for smooth user interaction.  The project also relies on environment configuration through a .env file, and I wrote automated tests to validate health checks and program functionality. Finally, the entire system is containerized with Docker, which ensures that the application is portable and self-contained. 

**Architecture Diagram:**

<img width="700" height="500" alt="architecture_diagram" src="https://github.com/user-attachments/assets/8792cf04-a67f-420a-923f-c4f87cf7a3ab" />


**Diagram description:** The architecture consists of three main layers: a data layer storing quotes in JSON format, a Python/Flask backend that exposes the API endpoints, and a simple HTML/JavaScript frontend served directly through Flask templates. Docker wraps all of these components together as the container.

**Data/Models/Services:** The API utilizes a small dataset of quotes stored as a JSON file in the ‘/assets’ folder. Each entry includes the quote, its author, and the category it is affiliated with. The file size is minimal, making it efficient to load and serve. The frontend uses a HTML template that produces a simplistic webpage. All services are open source, and the quotes come from freely available sources or public domain content. No external databases or third party APIs are required, reducing security concerns and simplifying deployment.

## **3) How to Run (Local)**

To run this project locally, Docker is the supported method. Once Docker is installed, the entire system can be built and run with a short sequence of commands.


1. Make the entry script executable:

```bash
chmod +x run.sh
```

2. Build the image:

```bash
docker build -t final-case:latest .
```
4. Run the container, mapping any free host port (example uses 5500) to the app’s internal port 8080:

```bash
docker run --rm -p 5500:8080 final-case:latest
```

6. Open the app in your browser at ‘http://localhost:5500 ’. If that host port is already in use, stop the other container (‘docker stop <**id**>’) or pick another port by changing the left side of ‘-p’, e.g. ‘-p 5501:8080’.

7. Health check: In the terminal, you can check the health using:

```bash
curl http://localhost:5500/health
```

You can also check the health in your browser once the website is running by simply typing in:
  http://localhost:5500/health

*Note: make sure you replace 5500 with whatever port you map it to initially.

## **4) Design Decisions**

**Why this concept:** I chose Flask because it is lightweight and minimalist, which is ideal for my learning and understanding of web development. Its flexibility allowed me to add only the components I needed, making my code clean and efficient. Flask allowed for easy integration of the frontend to the JSON endpoints and proved to be suitable for a project of my size. Additionally, I chose Docker as the container because it allows the project to be portable, reproducible, and easy to deploy across different systems. I thought this combination of concepts would deepen my understanding of the course material while allowing me to play around with the different components.
An alternative I considered, but did not end up using, was FastAPI. FastAPI is built on ASGI (Asynchronous Server Gateway Interface), making it asynchronous and generally more efficient than Flask. Flask, built on WSGI, is synchronous and processes on request at a time. However, I ultimately chose Flask over FastAPI because Flask is simpler and sufficient for this small app.

**Tradeoffs:** The main tradeoff for this project is between simplicity and scalability. The current setup is simple for the purposes of running and understanding the app, but it is not optimized for large datasets or high-traffic workloads. Storing data in a JSON file is fast and simple, but would cause problems if the quote dataset was more expansive, with thousands or even millions of quotes. The architecture prioritizes maintainability, low complexity, and low cost, as making adjustments is a simple process, and no external services are used that would require additional costs.

**Security/Privacy:** The Motivational Quote API uses a .env file to store configuration settings, rather than having secrets in the code. The API does not process any personal information (PII), and includes only minimal input validation for the category filters. Since the program is contained inside Docker, the application is further isolated from the host system.

**Ops:** The application has a /health endpoint for simple monitoring. Metrics can be expanded in any future versions to include request counts or performance tracking. The limitations of the current version include lack of authentication, scaling controls, or persistent logs. This means that there is no restriction on who can access the endpoints, the app is unable to handle many users at once, and the logs produced by the Flask app or Docker container disappear when the container stops.

## **5) Results & Evaluation**
   
The Motivational Quote API successfully delivers random or category-specific quotes, based on the request of the user on the dynamic frontend. During testing, the API responded quickly and consistently, using minimal memory due to the lightweight design. Below is a screenshot of the running frontend.

<img width="1319" height="241" alt="Screenshot 2025-12-01 at 2 36 02 PM" src="https://github.com/user-attachments/assets/910a00a1-9c7c-4740-86c3-f132ced2115d" />

**API sample output:**

http://localhost:5500/quote

{"author":"William James","category":"impact","quote":"Act as if what you do makes a difference. It does."}

**Validation and Tests:** I implemented tests into ‘tests/test_api.py’ to verify that quote retrieval works as expected and the API behaves correctly under typical usage patterns. Each test validates a specific feature of the API.

1. **test_health** sends a GET request to the /health endpoint, and confirms that the JSON response includes “‘status’: ‘ok’.” The health test ensures that the application is healthy and able to accept requests.
2. **test_quote_default** sends a GET request to /quote with no parameters to check that the response JSON includes a “quote” field. This test makes sure the API can return a random quote when the user does not supply a specific category.
3. **test_quote_category** sends a GET request to /quote?category=productivity, confirming that the JSON contains a “quote” field. This ensures that the API can successfully filter quotes by category and return a valid result.

## **6) What’s Next?**
Two improvements to this project that I would be interested in implementing would be expanding the quote dataset to have a wider variety to pull from, and refining the frontend to include animations and be more aesthetically pleasing. Some possible long-term enhancements include the ability to bookmark favorite quotes, integrating authentication, and deploying the project to a cloud platform to make it accessible to the public.

## **7) Links**

GitHub Repo: https://github.com/zoetankersley/final_case












