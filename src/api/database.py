"""
Database module for PaceLock.
Handles SQLite database operations including initialization, storage, and retrieval.
"""

import sqlite3
import json
from typing import Optional, Dict, Any
from datetime import datetime


def initialize_database(db_path: str = 'pacelock.db') -> sqlite3.Connection:
    """
    Initialize SQLite database for storing race data.
    Creates tables if they don't exist.
    
    Args:
        db_path: Path to the SQLite database file
        
    Returns:
        sqlite3.Connection: Database connection object
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create subsessions table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subsessions (
            subsession_id INTEGER PRIMARY KEY,
            session_name TEXT,
            track_name TEXT,
            start_time TEXT,
            data_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create lap_times table for future consistency analysis
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lap_times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subsession_id INTEGER,
            driver_id INTEGER,
            driver_name TEXT,
            lap_number INTEGER,
            lap_time REAL,
            lap_flags INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (subsession_id) REFERENCES subsessions (subsession_id)
        )
    ''')
    
    conn.commit()
    return conn


def store_subsession_data(conn: sqlite3.Connection, subsession_id: int, subsession_data: Dict[Any, Any]) -> bool:
    """
    Store subsession data in the database.
    
    Args:
        conn: Database connection
        subsession_id: ID of the subsession
        subsession_data: Raw subsession data from iRacing API
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        cursor = conn.cursor()
        
        # Extract relevant information from subsession data
        session_name = subsession_data.get('session_name', 'Unknown')
        track_info = subsession_data.get('track', {})
        track_name = track_info.get('track_name', 'Unknown')
        start_time = subsession_data.get('start_time', '')
        
        # Store the complete data as JSON for now
        data_json = json.dumps(subsession_data, default=str)
        
        cursor.execute('''
            INSERT OR REPLACE INTO subsessions 
            (subsession_id, session_name, track_name, start_time, data_json)
            VALUES (?, ?, ?, ?, ?)
        ''', (subsession_id, session_name, track_name, start_time, data_json))
        
        conn.commit()
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to store subsession data: {str(e)}")
        return False


def get_subsession_data(conn: sqlite3.Connection, subsession_id: int) -> Optional[Dict[Any, Any]]:
    """
    Retrieve subsession data from the database.
    
    Args:
        conn: Database connection
        subsession_id: ID of the subsession to retrieve
        
    Returns:
        Dict or None: Subsession data if found, None otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT data_json FROM subsessions 
            WHERE subsession_id = ?
        ''', (subsession_id,))
        
        row = cursor.fetchone()
        if row:
            return json.loads(row[0])
        return None
        
    except Exception as e:
        print(f"ERROR: Failed to retrieve subsession data: {str(e)}")
        return None


def list_stored_subsessions(conn: sqlite3.Connection) -> list:
    """
    Get list of all stored subsessions with basic info.
    
    Args:
        conn: Database connection
        
    Returns:
        list: List of tuples containing (subsession_id, session_name, track_name, created_at)
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT subsession_id, session_name, track_name, created_at 
            FROM subsessions 
            ORDER BY created_at DESC
        ''')
        
        return cursor.fetchall()
        
    except Exception as e:
        print(f"ERROR: Failed to list subsessions: {str(e)}")
        return []


def store_lap_times(conn: sqlite3.Connection, subsession_id: int, lap_data: Dict[Any, Any]) -> bool:
    """
    Store lap time data in the database.
    This will be used for future consistency analysis.
    
    Args:
        conn: Database connection
        subsession_id: ID of the subsession
        lap_data: Lap time data from iRacing API
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        cursor = conn.cursor()
        
        # This is a placeholder for when we implement lap time storage
        # The actual implementation will depend on the structure of lap_data
        print(f"TODO: Implement lap time storage for subsession {subsession_id}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to store lap times: {str(e)}")
        return False