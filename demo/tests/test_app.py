import pytest
from ..app import format_prompt, solve_problem

def test_format_prompt():
    """Test prompt formatting"""
    problem = "2 + 2"
    expected = "<|im_start|>user\nCan you help me solve this math problem? 2 + 2<|im_end|>\n"
    assert format_prompt(problem) == expected

def test_solve_problem_empty_input():
    """Test handling of empty input"""
    result = solve_problem("", "Custom")
    assert result == ("Please enter a problem", "Please enter a problem")

def test_solve_problem_with_type():
    """Test problem solving with specific type"""
    problem = "2 + 2"
    problem_type = "Addition"
    base_response, finetuned_response = solve_problem(problem, problem_type)
    
    # Check that responses are strings
    assert isinstance(base_response, str)
    assert isinstance(finetuned_response, str)
    
    # Check that responses are not error messages
    assert not base_response.startswith("Error")
    assert not finetuned_response.startswith("Error")

@pytest.mark.parametrize("problem_type", ["Addition", "Root Finding", "Derivative", "Custom"])
def test_solve_problem_types(problem_type):
    """Test problem solving with different types"""
    problem = "test problem"
    base_response, finetuned_response = solve_problem(problem, problem_type)
    
    # Check that responses are strings
    assert isinstance(base_response, str)
    assert isinstance(finetuned_response, str)
