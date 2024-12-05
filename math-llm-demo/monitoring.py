import time
from datetime import datetime
import json
import os
from collections import defaultdict
import threading
import numpy as np

class PerformanceMonitor:
    def __init__(self, metrics_file="metrics.json"):
        self.metrics_file = metrics_file
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
        self._load_metrics()
    
    def _load_metrics(self):
        """Load existing metrics from file"""
        if os.path.exists(self.metrics_file):
            try:
                with open(self.metrics_file, 'r') as f:
                    self.metrics.update(json.load(f))
            except json.JSONDecodeError:
                pass
    
    def _save_metrics(self):
        """Save metrics to file"""
        with self.lock:
            with open(self.metrics_file, 'w') as f:
                json.dump(dict(self.metrics), f)
    
    def record_response_time(self, model_id, duration):
        """Record response time for a model"""
        with self.lock:
            self.metrics[f"{model_id}_response_times"].append({
                'timestamp': datetime.now().isoformat(),
                'duration': duration
            })
            self._save_metrics()
    
    def record_success(self, model_id, success):
        """Record success/failure for a model"""
        with self.lock:
            self.metrics[f"{model_id}_success_rate"].append({
                'timestamp': datetime.now().isoformat(),
                'success': success
            })
            self._save_metrics()
    
    def record_problem_type(self, problem_type):
        """Record usage of different problem types"""
        with self.lock:
            self.metrics['problem_types'].append({
                'timestamp': datetime.now().isoformat(),
                'type': problem_type
            })
            self._save_metrics()
    
    def get_statistics(self):
        """Calculate and return performance statistics"""
        stats = {}
        
        # Response time statistics
        for model in ['base', 'finetuned']:
            times = [x['duration'] for x in self.metrics.get(f"{model}_response_times", [])]
            if times:
                stats[f"{model}_avg_response_time"] = np.mean(times)
                stats[f"{model}_max_response_time"] = np.max(times)
                stats[f"{model}_min_response_time"] = np.min(times)
        
        # Success rate statistics
        for model in ['base', 'finetuned']:
            successes = [x['success'] for x in self.metrics.get(f"{model}_success_rate", [])]
            if successes:
                stats[f"{model}_success_rate"] = sum(successes) / len(successes) * 100
        
        # Problem type distribution
        problem_types = [x['type'] for x in self.metrics.get('problem_types', [])]
        if problem_types:
            type_counts = defaultdict(int)
            for ptype in problem_types:
                type_counts[ptype] += 1
            total = len(problem_types)
            stats['problem_type_distribution'] = {
                ptype: (count / total) * 100 
                for ptype, count in type_counts.items()
            }
        
        return stats

def measure_time(func):
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        return result, duration
    return wrapper
