---
title: Math Problem Solver Demo
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Mathematics Problem Solver Demo

This demo showcases a comparison between base and fine-tuned language models in solving mathematical problems. It features real-time performance monitoring and supports multiple types of math problems.

## Models Used

- Base Model: [LlaMA 3.2 1B](https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1B-GGUF)
- Fine-tuned Model: [SmolLM2 1.7B](https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1.7B-GGUF)

## Features

- 🔢 Multiple problem types:
  - Addition operations
  - Root finding
  - Derivatives
  - Custom problems
- 📊 Real-time performance metrics:
  - Response times
  - Success rates
  - Problem type distribution
- 🔄 Side-by-side model comparison
- ⚡ Example problems included

## How to Use

1. Select a problem type from the dropdown menu
2. Enter your math problem in the input field
3. Click "Solve" to see solutions from both models
4. Compare the results and view performance metrics

## Example Problems

Try these sample problems:

- Derivative: "Find the derivative of x^2 + 3x"
- Root Finding: "What is the square root of 144?"
- Addition: "Calculate 235 + 567"

## Performance Monitoring

The interface includes a live dashboard showing:

- Average response times for each model
- Success rates comparison
- Distribution of problem types solved
- Real-time performance metrics

## Project Details

This demo is part of a larger project comparing LLM performance on mathematical problems. The models have been fine-tuned on a custom dataset of mathematical problems to improve their problem-solving capabilities.

## Credits

Models provided by [Alexis-Az](https://huggingface.co/Alexis-Az)
