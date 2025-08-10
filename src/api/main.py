#!/usr/bin/env python3
"""
PaceLock - iRacing Consistency Analytics
Main script for loading and analyzing iRacing subsession data.
"""

from .iracing_api import load_subsession_data
from .database import initialize_database, store_subsession_data

def main():
    """Main entry point."""
    print("PaceLock - iRacing Consistency Analytics")
    print("=" * 40)
    
    # Hardcoded subsession ID for initial testing
    SUBSESSION_ID = 78923458
    
    # Initialize database
    print("Initializing database...")
    conn = initialize_database()
    
    # Load subsession data
    subsession_data = load_subsession_data(SUBSESSION_ID)
    
    if subsession_data:
        # Store in database
        if store_subsession_data(conn, SUBSESSION_ID, subsession_data):
            print(f"✓ Data stored in database")
        else:
            print(f"⚠ Warning: Failed to store data in database")
        
        # Basic data exploration
        display_subsession_summary(subsession_data)
    else:
        print("Failed to load subsession data. Exiting.")
        exit(1)
    
    conn.close()
    print("\n✓ Process completed successfully")


def display_subsession_summary(subsession_data: dict) -> None:
    """
    Display a summary of the subsession data.
    
    Args:
        subsession_data: Raw subsession data from iRacing API
    """
    session_results = subsession_data.get('session_results', [])
    if session_results:
        print(f"\nTop 5 finishers:")
        for result in session_results[:5]:
            driver_name = result.get('display_name', 'Unknown')
            finish_pos = result.get('finish_position', 'N/A')
            print(f"  {finish_pos}. {driver_name}")
    
    # Additional session info
    print(f"\nSession Details:")
    print(f"  Session Name: {subsession_data.get('session_name', 'Unknown')}")
    track_info = subsession_data.get('track', {})
    print(f"  Track: {track_info.get('track_name', 'Unknown')}")
    print(f"  Total Entries: {len(session_results)}")
    
    if 'start_time' in subsession_data:
        print(f"  Start Time: {subsession_data['start_time']}")
    if 'end_time' in subsession_data:
        print(f"  End Time: {subsession_data['end_time']}")


if __name__ == "__main__":
    main()