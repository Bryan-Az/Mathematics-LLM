# Mathematics-LLM
This is a brief group project where we train and benchmark a LLM on it's ability to respond accurately to math problems.
**Key Words** LLMOps, GenAI, SmolLM2, LLama, Mathematics, Problem Solving, LLMs
## Abstract
Large language models (LLMs) like GPT-3 excel in generating and understanding text but encounter significant limitations when dealing with tasks that require precise logical reasoning or numerical analysis, such as solving mathematical problems. These models often struggle with symbolic manipulation and can misinterpret the specific requirements of math-related queries due to their design focusing on linguistic, rather than numerical, understanding. The goal of our project is to deliver a full LLM-OPs pipeline and train, evaluate repective LLMs to respond to math problems in a numerical/LaTex output. 

## Data
### Training / Evaluation Datasets

Subsets for additions, derivaties, and roots: https://huggingface.co/datasets/Alexis-Az/math_datasets

### Evaluation Metrics Dataset

Evaluations for Both Models: https://huggingface.co/datasets/Alexis-Az/Math-LLM-Evaluations
## Finetuning  HuggingFace Links

### Finetuning Education/Math HuggingFaceTB SmolLM2 1.7B Parameter Model

base model: https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct 

non-quantized model: https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1.7B

quantized model: https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1.7B-GGUF


### Finetuning Base LlaMA 3.2 1B Parameter Model

base model: https://huggingface.co/unsloth/Llama-3.2-1B-Instruct

quantized model: https://huggingface.co/Alexis-Az/Math-Problem-LlaMA-3.2-1B-GGUF


## Demo Link
https://www.youtube.com/watch?v=wdbirGmC2wI 

