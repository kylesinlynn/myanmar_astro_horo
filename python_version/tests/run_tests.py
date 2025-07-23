#!/usr/bin/env python3
"""
Test runner for Myanmar Astro Horo Python version
Runs all unit tests and generates a comprehensive test report
"""

import unittest
import sys
import os
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import test modules
from test_astronomical_calculations import TestAstronomicalCalculations, TestAstronomicalAccuracy
from test_myanmar_calendar import TestMyanmarCalendarSystem, TestMyanmarCalendarAccuracy
from test_horoscope_generator import TestHoroscopeGenerator, TestHoroscopeAccuracy


def run_all_tests():
    """Run all test suites and generate report"""
    print("Myanmar Astro Horo - Python Version Test Suite")
    print("=" * 50)
    print(f"Test run started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_classes = [
        TestAstronomicalCalculations,
        TestAstronomicalAccuracy,
        TestMyanmarCalendarSystem,
        TestMyanmarCalendarAccuracy,
        TestHoroscopeGenerator,
        TestHoroscopeAccuracy
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0]}")
    
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('\\n')[-2]}")
    
    print(f"\nTest run completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Return success status
    return len(result.failures) == 0 and len(result.errors) == 0


def run_specific_test(test_name):
    """Run a specific test module"""
    test_modules = {
        'astro': 'test_astronomical_calculations',
        'calendar': 'test_myanmar_calendar', 
        'horoscope': 'test_horoscope_generator'
    }
    
    if test_name in test_modules:
        module_name = test_modules[test_name]
        print(f"Running {module_name} tests...")
        
        # Import and run specific module
        module = __import__(module_name)
        unittest.main(module=module, verbosity=2, exit=False)
    else:
        print(f"Unknown test module: {test_name}")
        print(f"Available modules: {', '.join(test_modules.keys())}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Run specific test
        run_specific_test(sys.argv[1])
    else:
        # Run all tests
        success = run_all_tests()
        sys.exit(0 if success else 1)
