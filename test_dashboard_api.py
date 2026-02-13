"""
Test script to verify dynamic dashboard functionality
Run this after starting the backend server
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_dashboard_stats():
    """Test the new dashboard stats endpoint"""
    print("=" * 60)
    print("Testing Dashboard Stats Endpoint")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/dashboard/stats")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS - Dashboard stats endpoint is working!\n")
            print("Dashboard Statistics:")
            print(f"  📊 Total Audits: {data['total_audits']}")
            print(f"  ✅ Passed Messages: {data['passed_messages']}")
            print(f"  ❌ Failed Messages: {data['failed_messages']}")
            print(f"  ⚡ Validation Quality: {data['validation_quality']}%")
            print()
            
            # Verify calculation
            if data['total_audits'] > 0:
                expected_quality = round((data['passed_messages'] / data['total_audits']) * 100)
                if data['validation_quality'] == expected_quality:
                    print("✅ Validation quality calculation is correct!")
                else:
                    print(f"⚠️ Quality calculation mismatch: {data['validation_quality']} vs {expected_quality}")
            else:
                print("ℹ️ No validation records found in database")
            
            return True
        else:
            print(f"❌ FAILED - Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ ERROR - Cannot connect to backend server")
        print(f"Make sure the backend is running on {BASE_URL}")
        return False
    except Exception as e:
        print(f"❌ ERROR - {str(e)}")
        return False

def test_history_endpoint():
    """Test the history endpoint with limit"""
    print("\n" + "=" * 60)
    print("Testing History Endpoint (Recent Activity)")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/history?limit=5")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS - Retrieved {len(data)} recent records\n")
            
            if len(data) > 0:
                print("Recent Validations:")
                for i, record in enumerate(data[:3], 1):  # Show first 3
                    print(f"\n  {i}. Validation ID: {record['validation_id']}")
                    print(f"     Message Type: {record['message_type']}")
                    print(f"     Status: {record['status']}")
                    print(f"     Errors: {record['total_errors']}")
                    print(f"     Warnings: {record['total_warnings']}")
                
                if len(data) > 3:
                    print(f"\n  ... and {len(data) - 3} more records")
            else:
                print("ℹ️ No validation history found")
            
            return True
        else:
            print(f"❌ FAILED - Status Code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR - {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "🧪 DYNAMIC DASHBOARD API TESTS")
    print("=" * 60 + "\n")
    
    # Test dashboard stats
    stats_ok = test_dashboard_stats()
    
    # Test history endpoint
    history_ok = test_history_endpoint()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Dashboard Stats: {'✅ PASS' if stats_ok else '❌ FAIL'}")
    print(f"History Endpoint: {'✅ PASS' if history_ok else '❌ FAIL'}")
    
    if stats_ok and history_ok:
        print("\n🎉 All tests passed! Dashboard is fully dynamic and working!")
        print("\nNext step: Open http://localhost:4200 to see the live dashboard")
    else:
        print("\n⚠️ Some tests failed. Check the backend server.")
    
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
