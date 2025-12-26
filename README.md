# Game of Life (Web / WebSocket Edition)

A browser-based implementation of **Conway’s Game of Life**, built using **Python**, **FastAPI**, and **WebSockets**.

This project started as a pygame learning exercise and later evolved into an experiment in separating **simulation logic** from **presentation**, while exploring how real-time systems communicate between a backend and a browser frontend.

The goal is **not performance or polish**, but understanding how data flows through a system.


---

## About this project

This version of the Game of Life runs in the browser, while the simulation itself runs on the server.

The browser acts as a **viewer**:
- receives updates from the server  
- draws the grid  
- does not contain game logic  

The server:
- maintains the grid state  
- applies Conway’s rules  
- streams updates using WebSockets  

This clean separation makes it easier to reason about the system and reuse logic elsewhere.

---

## Project structure

game-of-life-web/
├── life.py # Core Game of Life logic (shared, UI-agnostic)
├── server.py # FastAPI + WebSocket server
├── web/
│ └── index.html # Browser frontend
└── README.md


---

## Game rules

Conway’s Game of Life follows three simple rules:

### Survival  
A live cell survives if it has **2 or 3** live neighbors.

### Death  
A live cell dies if it has **fewer than 2** or **more than 3** neighbors.

### Birth  
A dead cell becomes alive if it has **exactly 3** neighbors.

Despite these simple rules, complex and interesting patterns emerge over time.

---

## How it works

### Backend (Python)
- Maintains the grid state  
- Computes the next generation  
- Sends the grid to connected clients via WebSockets  

### Frontend (Browser)
- Receives grid updates  
- Renders the grid using `<canvas>`  
- Updates in real time  

The browser never modifies the simulation directly — it only visualizes it.

---

## Running the project (local)

### Requirements

- Python **3.8+**
- `fastapi`
- `uvicorn`

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

### Start the server


uvicorn server:app --host 0.0.0.0 --reload
```

Then open in your browser:

http://localhost:8000

---

## Running with Docker (project goal)

One of the goals of this project is to make it **fully self-contained** and runnable using Docker.

Eventually, the application should be runnable with:

bash: docker compose up

This will:
- build the image  
- start the FastAPI server  
- expose the application on port 8000  

No local Python installation required.

---

### Planned Docker setup

The goal is to keep things simple:

- A single container running:
  - FastAPI  
  - WebSocket server  
  - Game of Life simulation  
- Port 8000 exposed  
- No external dependencies  

This makes the project easy to run, share, and experiment with.

---

## Features

- Real-time simulation using WebSockets  
- Clean separation between logic and UI  
- No JavaScript frameworks  
- Simple, readable code  
- Easy to extend  
- Designed with containerization in mind  

---

## Design philosophy

This project is intentionally:
- simple  
- explicit  
- readable  

It favors clarity over abstraction and avoids unnecessary complexity.

The goal is learning — not optimization.

---

## Why WebSockets?

WebSockets allow:
- continuous updates without polling  
- low-latency communication  
- a clear mental model for real-time systems  

They are well suited for visual simulations like the Game of Life.

---

## Relationship to the pygame version

This project complements the original pygame-based implementation.

- pygame version → learning rendering, input handling, and game loops  
- web version → learning networking, async systems, and separation of concerns  

Both versions share the same core simulation logic.

---

## Future ideas

Possible next steps:
- Click to toggle cells  
- Pause / resume controls  
- Adjustable simulation speed  
- Multiple connected viewers  
- Saving and loading patterns  
- Publishing a Docker image  

---

## Inspiration

Conway’s Game of Life explained by its creator:  
https://www.youtube.com/watch?v=R9Plq-D1gEk

---

## Notes

This project is intentionally small and readable.  
It is meant as a learning tool, not a framework.
