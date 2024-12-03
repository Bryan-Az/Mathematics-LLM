import pytest
import os
import json
from ..monitoring import PerformanceMonitor, measure_time
import time

@pytest.fixture
def monitor():
    """Create a test monitor instance with a temporary metrics file"""
    test_file = "test_metrics.json"
    monitor = PerformanceMonitor(metrics_file=test_file)
    yield monitor
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

def test_record_response_time(monitor):
    """Test recording response times"""
    monitor.record_response_time("base", 1.5)
    monitor.record_response_time("finetuned", 1.2)
    
    stats = monitor.get_statistics()
    assert 'base_avg_response_time' in stats
    assert 'finetuned_avg_response_time' in stats
    assert abs(stats['base_avg_response_time'] - 1.5) < 0.001
    assert abs(stats['finetuned_avg_response_time'] - 1.2) < 0.001

def test_record_success(monitor):
    """Test recording success rates"""
    monitor.record_success("base", True)
    monitor.record_success("base", False)
    monitor.record_success("finetuned", True)
    
    stats = monitor.get_statistics()
    assert 'base_success_rate' in stats
    assert 'finetuned_success_rate' in stats
    assert abs(stats['base_success_rate'] - 50.0) < 0.001  # 1/2 success
    assert abs(stats['finetuned_success_rate'] - 100.0) < 0.001  # 1/1 success

def test_record_problem_type(monitor):
    """Test recording problem type distribution"""
    monitor.record_problem_type("Addition")
    monitor.record_problem_type("Derivative")
    monitor.record_problem_type("Addition")
    
    stats = monitor.get_statistics()
    assert 'problem_type_distribution' in stats
    distribution = stats['problem_type_distribution']
    assert abs(distribution['Addition'] - 66.67) < 0.01  # 2/3
    assert abs(distribution['Derivative'] - 33.33) < 0.01  # 1/3

def test_measure_time_decorator():
    """Test the measure_time decorator"""
    @measure_time
    def slow_function():
        time.sleep(0.1)
        return "result"
    
    result, duration = slow_function()
    assert result == "result"
    assert duration >= 0.1

def test_metrics_persistence(monitor):
    """Test that metrics are saved to and loaded from file"""
    # Record some metrics
    monitor.record_response_time("base", 1.0)
    monitor.record_success("base", True)
    
    # Create new monitor instance with same file
    new_monitor = PerformanceMonitor(metrics_file=monitor.metrics_file)
    
    # Check if metrics were loaded
    stats = new_monitor.get_statistics()
    assert 'base_avg_response_time' in stats
    assert 'base_success_rate' in stats

def test_concurrent_access(monitor):
    """Test thread safety of metrics recording"""
    import threading
    
    def record_metrics():
        for _ in range(100):
            monitor.record_response_time("base", 1.0)
    
    threads = [threading.Thread(target=record_metrics) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    stats = monitor.get_statistics()
    assert len(monitor.metrics["base_response_times"]) == 500  # 5 threads * 100 records

def test_error_handling(monitor):
    """Test handling of invalid metrics file"""
    # Create invalid JSON file
    with open(monitor.metrics_file, 'w') as f:
        f.write("invalid json")
    
    # Should not raise exception when loading invalid file
    new_monitor = PerformanceMonitor(metrics_file=monitor.metrics_file)
    assert isinstance(new_monitor.metrics, dict)
