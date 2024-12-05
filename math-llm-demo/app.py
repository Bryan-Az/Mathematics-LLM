import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Model configurations
BASE_MODEL = "Alexis-Az/Math-Problem-LlaMA-3.2-1B"  # Public LLaMA model
OUR_ADAPTER = "Joash2024/Math-SmolLM2-1.7B"        # Our LoRA adapter

# Configure quantization
bnb_config = BitsAndBytesConfig(
    load_in_8bit=True,
)

# Load tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
tokenizer.pad_token = tokenizer.eos_token

# Load base model and adapter
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=bnb_config,
    device_map="auto",
    torch_dtype=torch.float16
)

print("Loading LoRA adapter...")
model = PeftModel.from_pretrained(model, OUR_ADAPTER)
model.eval()

def format_prompt(operation: str, problem: str) -> str:
    """Format input prompt for the model"""
    if operation == "Derivative":
        return f"""Given a mathematical function, find its derivative.

Function: {problem}
The derivative of this function is:"""
    elif operation == "Addition":
        return f"""Solve this addition problem.

Problem: {problem}
The solution is:"""
    else:  # Roots
        return f"""Find the roots of this equation.

Equation: {problem}
The roots are:"""

def generate_solution(operation: str, problem: str, max_length: int = 200) -> str:
    """Generate solution for a given problem"""
    # Format the prompt
    prompt = format_prompt(operation, problem)
    
    # Tokenize
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # Generate
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode and extract solution
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    solution = generated[len(prompt):].strip()
    
    return solution

# Create Gradio interface
def solve_problem(operation: str, problem: str) -> str:
    """Solve a mathematical problem"""
    try:
        solution = generate_solution(operation, problem)
        return solution
    except Exception as e:
        return f"Error: {str(e)}"

# Define interface
iface = gr.Interface(
    fn=solve_problem,
    inputs=[
        gr.Dropdown(
            choices=["Derivative", "Addition", "Roots"],
            label="Operation"
        ),
        gr.Textbox(
            lines=2,
            placeholder="Enter your mathematical problem...",
            label="Problem"
        )
    ],
    outputs=gr.Textbox(label="Solution"),
    title="Mathematics Problem Solver",
    description="""This app can:
    1. Find derivatives of functions (e.g., x^2, sin(x))
    2. Solve addition problems
    3. Find roots of equations
    
    Use LaTeX notation for mathematical expressions (e.g., x^2, \\sin{\\left(x\\right)})""",
    examples=[
        ["Derivative", "x^2"],
        ["Derivative", "\\sin{\\left(x\\right)}"],
        ["Derivative", "e^x"],
        ["Addition", "123 + 456"],
        ["Roots", "x^2 - 4"]
    ]
)

# Launch app
if __name__ == "__main__":
    iface.launch()
