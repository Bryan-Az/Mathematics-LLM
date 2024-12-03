import gradio as gr
from transformers import AutoTokenizer, pipeline
import torch

# Model IDs
BASE_MODEL_ID = "Alexis-Az/Math-Problem-LlaMA-3.2-1B-GGUF"
FINETUNED_MODEL_ID = "Alexis-Az/Math-Problem-LlaMA-3.2-1.7B-GGUF"

def format_prompt(problem):
    """Format the input problem according to the model's expected format"""
    return f"<|im_start|>user\nCan you help me solve this math problem? {problem}<|im_end|>\n"

def get_model_response(problem, model_id):
    """Get response from a specific model"""
    try:
        # Initialize pipeline
        pipe = pipeline(
            "text-generation",
            model=model_id,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        
        # Format prompt and generate response
        prompt = format_prompt(problem)
        response = pipe(
            prompt,
            max_new_tokens=100,
            temperature=0.1,
            top_p=0.95,
            repetition_penalty=1.15
        )[0]["generated_text"]
        
        # Extract assistant's response
        assistant_response = response.split("<|im_start|>assistant\n")[-1].split("<|im_end|>")[0]
        return assistant_response.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def solve_problem(problem, problem_type):
    """Solve a math problem using both models"""
    if not problem:
        return "Please enter a problem", "Please enter a problem"
    
    # Add problem type context if provided
    if problem_type != "Custom":
        problem = f"{problem_type}: {problem}"
    
    # Get responses from both models
    base_response = get_model_response(problem, BASE_MODEL_ID)
    finetuned_response = get_model_response(problem, FINETUNED_MODEL_ID)
    
    return base_response, finetuned_response

# Create Gradio interface
with gr.Blocks(title="Mathematics Problem Solver") as demo:
    gr.Markdown("# Mathematics Problem Solver")
    gr.Markdown("Compare solutions between base (1B) and fine-tuned (1.7B) models")
    
    with gr.Row():
        with gr.Column():
            problem_type = gr.Dropdown(
                choices=["Addition", "Root Finding", "Derivative", "Custom"],
                value="Custom",
                label="Problem Type"
            )
            problem_input = gr.Textbox(
                label="Enter your math problem",
                placeholder="Example: Find the derivative of x^2 + 3x"
            )
            solve_btn = gr.Button("Solve", variant="primary")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Base Model (1B)")
            base_output = gr.Textbox(label="Base Model Solution", lines=5)
        
        with gr.Column():
            gr.Markdown("### Fine-tuned Model (1.7B)")
            finetuned_output = gr.Textbox(label="Fine-tuned Model Solution", lines=5)
    
    # Example problems
    gr.Examples(
        examples=[
            ["Find the derivative of x^2 + 3x", "Derivative"],
            ["What is the square root of 144?", "Root Finding"],
            ["Calculate 235 + 567", "Addition"],
        ],
        inputs=[problem_input, problem_type],
        outputs=[base_output, finetuned_output],
        fn=solve_problem,
        cache_examples=True,
    )
    
    # Connect the interface
    solve_btn.click(
        fn=solve_problem,
        inputs=[problem_input, problem_type],
        outputs=[base_output, finetuned_output]
    )

if __name__ == "__main__":
    demo.launch()
