# Mathematics Problem Solver Demo

This is a Gradio-based web interface for comparing the mathematics problem-solving capabilities of our base and fine-tuned language models.

## Features

- Interactive web interface
- Support for multiple problem types:
  - Addition operations
  - Root finding
  - Derivatives
  - Custom problems
- Side-by-side model comparison
- Example problems included
- Error handling and validation
- Automated testing
- Continuous Integration with GitHub Actions

## Models Used

- Base Model: LlaMA 3.2 1B ([Alexis-Az/Math-Problem-LlaMA-3.2-1B-GGUF](https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1B-GGUF))
- Fine-tuned Model: SmolLM2 1.7B ([Alexis-Az/Math-Problem-LlaMA-3.2-1.7B-GGUF](https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1.7B-GGUF))

## Local Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:7860)

## Testing

### Running Tests Locally

1. Using the test script:

```bash
./run_tests.sh
```

2. Or manually with pytest:

```bash
pytest --cov=. --cov-report=term-missing --cov-report=html
```

### Automated Testing

- Tests run automatically on GitHub Actions when:
  - Pushing to main branch
  - Creating a pull request to main
  - Pushing to feature branches
- Coverage reports are generated and uploaded to Codecov

## HuggingFace Spaces Deployment

This demo can be deployed to HuggingFace Spaces for free:

1. Create a new Space on HuggingFace:

   - Go to huggingface.co/spaces
   - Click "Create new Space"
   - Select "Gradio" as the SDK
   - Choose a name for your Space

2. Upload these files to your Space:

   - app.py
   - requirements.txt

3. The interface will be automatically deployed and accessible via a public URL

## Usage

1. Select a problem type from the dropdown (Addition, Root Finding, Derivative, or Custom)
2. Enter your math problem in the input field
3. Click "Solve" to get solutions from both models
4. Compare the results side by side

## Example Problems

The interface includes several example problems that you can try:

- Derivative problems (e.g., "Find the derivative of x^2 + 3x")
- Root finding problems (e.g., "What is the square root of 144?")
- Addition problems (e.g., "Calculate 235 + 567")

## Error Handling

The interface includes robust error handling:

- Input validation
- Model loading error handling
- Response parsing error handling

## Performance Monitoring

The interface can be extended with:

- Success rate tracking
- Response time monitoring
- Accuracy comparisons between models
- Usage statistics

## Contributing

To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure tests pass locally
5. Submit a pull request

## Future Improvements

Planned enhancements:

- Add support for more problem types
- Implement performance metrics display
- Add solution step breakdown
- Include confidence scores for answers
- Add real-time performance monitoring
- Expand test coverage
