from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

# Initialize FastAPI app
app = FastAPI()

# Connect to SQLite database
DATABASE = 'identities.db'

# Ensure database and table exist
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE UserIdentity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        did TEXT NOT NULL,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE VerificationResult (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identity_id INTEGER NOT NULL,
        verified BOOLEAN NOT NULL,
        timestamp DATETIME NOT NULL,
        FOREIGN KEY(identity_id) REFERENCES UserIdentity(id)
    )
    ''')
    # Seed data
    cursor.execute("INSERT INTO UserIdentity (did, name, email) VALUES ('did:example:123', 'Alice', 'alice@example.com')")
    cursor.execute("INSERT INTO VerificationResult (identity_id, verified, timestamp) VALUES (1, 1, ?)" , (datetime.now(),))
    conn.commit()
    conn.close()

# Pydantic models
class UserIdentity(BaseModel):
    id: int
    did: str
    name: str
    email: str

class VerificationResult(BaseModel):
    id: int
    identity_id: int
    verified: bool
    timestamp: datetime

# API Endpoints
@app.post("/api/identities", response_model=UserIdentity)
def create_identity(identity: UserIdentity):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserIdentity (did, name, email) VALUES (?, ?, ?)", (identity.did, identity.name, identity.email))
    conn.commit()
    identity_id = cursor.lastrowid
    conn.close()
    return {"id": identity_id, **identity.dict()}

@app.get("/api/identities", response_model=List[UserIdentity])
def get_identities():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserIdentity")
    rows = cursor.fetchall()
    conn.close()
    return [UserIdentity(id=row[0], did=row[1], name=row[2], email=row[3]) for row in rows]

@app.get("/api/identities/{identity_id}", response_model=UserIdentity)
def get_identity(identity_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserIdentity WHERE id = ?", (identity_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return UserIdentity(id=row[0], did=row[1], name=row[2], email=row[3])
    raise HTTPException(status_code=404, detail="Identity not found")

@app.post("/api/verify", response_model=VerificationResult)
def verify_identity(identity_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserIdentity WHERE id = ?", (identity_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Identity not found")
    # Mock verification logic
    verified = True  # Assume verification is successful
    timestamp = datetime.now()
    cursor.execute("INSERT INTO VerificationResult (identity_id, verified, timestamp) VALUES (?, ?, ?)", (identity_id, verified, timestamp))
    conn.commit()
    verification_id = cursor.lastrowid
    conn.close()
    return VerificationResult(id=verification_id, identity_id=identity_id, verified=verified, timestamp=timestamp)

# Serve HTML pages
@app.get("/", response_class=HTMLResponse)
def read_root():
    return open('templates/index.html').read()

@app.get("/create-identity", response_class=HTMLResponse)
def create_identity_page():
    return open('templates/create_identity.html').read()

@app.get("/verify-identity", response_class=HTMLResponse)
def verify_identity_page():
    return open('templates/verify_identity.html').read()

@app.get("/identities", response_class=HTMLResponse)
def manage_identities_page():
    return open('templates/manage_identities.html').read()

@app.get("/about", response_class=HTMLResponse)
def about_page():
    return open('templates/about.html').read()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")
