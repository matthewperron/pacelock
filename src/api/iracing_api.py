"""
iRacing API integration module for PaceLock.
Handles authentication, API calls, and data retrieval from iRacing.
"""

import os
import sys
from typing import Optional
from dotenv import load_dotenv
from iracingdataapi.client import irDataClient


def check_environment() -> tuple[str, str]:
    """
    Check that required environment variables are set.
    Returns tuple of (username, password) if valid.
    Exits with error message if credentials are missing.
    """
    load_dotenv()
    
    username = os.getenv('IRACING_USERNAME')
    password = os.getenv('IRACING_PASSWORD')
    
    if not username or not password:
        print("ERROR: iRacing credentials not found!")
        print("")
        print("Please set the following environment variables:")
        print("  IRACING_USERNAME - Your iRacing username")
        print("  IRACING_PASSWORD - Your iRacing password")
        print("")
        print("You can either:")
        print("  1. Export them in your shell:")
        print("     export IRACING_USERNAME=your_username")
        print("     export IRACING_PASSWORD=your_password")
        print("")
        print("  2. Create a .env file with:")
        print("     IRACING_USERNAME=your_username")
        print("     IRACING_PASSWORD=your_password")
        print("")
        sys.exit(1)
    
    return username, password


def get_api_client() -> irDataClient:
    """
    Create and return authenticated iRacing API client.
    """
    username, password = check_environment()
    return irDataClient(username=username, password=password)


def load_subsession_data(subsession_id: int) -> Optional[dict]:
    """
    Load subsession data from iRacing API.
    Returns subsession data dict or None if failed.
    """
    try:
        print(f"Connecting to iRacing API...")
        idc = get_api_client()
        
        print(f"Loading subsession {subsession_id}...")
        subsession_data = idc.result(subsession_id)
        
        if subsession_data:
            print(f"Successfully loaded subsession data:")
            print(f"  Session: {subsession_data.get('session_name', 'Unknown')}")
            print(f"  Track: {subsession_data.get('track', {}).get('track_name', 'Unknown')}")
            print(f"  Entries: {len(subsession_data.get('session_results', []))}")
            return subsession_data
        else:
            print(f"ERROR: No data returned for subsession {subsession_id}")
            return None
            
    except Exception as e:
        error_msg = str(e)
        if "Legacy authorization refused" in error_msg:
            print(f"ERROR: iRacing Legacy Authorization Required!")
            print("")
            print("To use this API, you must enable legacy authentication in your iRacing account:")
            print("  1. Log into your iRacing account at https://members.iracing.com/")
            print("  2. Go to Account Settings") 
            print("  3. Find 'Allow applications to access your account via password'")
            print("  4. Check the box to enable legacy authentication")
            print("")
            print("Note: This is required for third-party applications to access iRacing data.")
        else:
            print(f"ERROR: Failed to load subsession data: {error_msg}")
        return None


def load_lap_times(subsession_id: int, cust_id: int = None) -> Optional[dict]:
    """
    Load lap time data for a specific subsession.
    Returns lap time data dict or None if failed.
    """
    try:
        print(f"Loading lap times for subsession {subsession_id}...")
        idc = get_api_client()
        
        if cust_id:
            lap_data = idc.result_lap_data(subsession_id=subsession_id, cust_id=cust_id)
        else:
            lap_data = idc.result_lap_data(subsession_id=subsession_id)
        
        if lap_data:
            print(f"Successfully loaded lap time data")
            return lap_data
        else:
            print(f"ERROR: No lap time data returned for subsession {subsession_id}")
            return None
            
    except Exception as e:
        print(f"ERROR: Failed to load lap time data: {str(e)}")
        return None